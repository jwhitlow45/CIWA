# Azure functions
from datetime import datetime
from os import stat
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import azure.functions as func

# Debugging and logging
import logging
import datetime
from requests import ConnectionError, HTTPError, Timeout

# Type management
import pydantic

# Shared objects
from shared.message import actions
from shared.raw_data.service import HourlyRawDataService as HRDS, DailyRawDataService as DRDS
from shared.core import config, utils


def main(msg: func.ServiceBusMessage):
    logging.info(f'raw_message_queue_receiver ran at {utils.get_utc_timestamp()}')

    try:
        # Store response in message string
        message = msg.get_body()
        # Parse json message into Action object
        action = pydantic.parse_raw_as(actions.Action, message)

        # Check if action is of type DATA_GET_HOURLY_RAW or DATA_GET_DAILY_RAW
        if action.action_type == actions.ActionType.DATA_ADD_HOURLY_RAW:
            # Update hourly data to SQL database
            action = pydantic.parse_raw_as(actions.AddHourlyRawDataAction,
                                            message)

            # If message is now below cimis record limit split to fit into record limit
            if not utils.is_below_cimis_record_limit(action.payload.station_ids,
                                                    utils.parse_date_str(action.payload.start_date),
                                                    utils.parse_date_str(action.payload.end_date),
                                                    config.CIMIS_API_HOURLY_RECORDS_PER_DAY):
                requests_as_list = utils.split_action(action)
                with ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
                    with client.get_queue_sender(config.SERVICE_BUS_RAW_QUEUE_NAME) as sender:
                        for new_action in requests_as_list:
                            new_msg = ServiceBusMessage(new_action.json())
                            sender.send_messages(new_msg)
                        logging.info(f'Split large message into smaller messages and sent to back of queue\
                            {config.SERVICE_BUS_RAW_QUEUE_NAME} at time {utils.get_utc_timestamp()}')
            
            else:
                # Get cimis reponse
                cimis_response = HRDS.get_hourlyraw_data_from_cimis(targets=action.payload.station_ids,
                                                                start_date=utils.parse_date_str(action.payload.start_date),
                                                                end_date=utils.parse_date_str(action.payload.end_date))
                logging.info(f'Received CIMIS response at {utils.get_utc_timestamp()}')
                rawdata_schema = HRDS.to_hourlyraw_schema(cimis_response)
                HRDS.insert_hourlyraw_data(rawdata_schema)
                logging.info(f'Successfully added data to dbo.HourlyRaw at {utils.get_utc_timestamp()}')                                                                   

        elif action.action_type == actions.ActionType.DATA_ADD_DAILY_RAW:
            # Update daily data to SQL database
            action = pydantic.parse_raw_as(actions.AddDailyRawDataAction,
                                            message)

            # If message is not below cimis record limit split to fitinto record limit
            if not utils.is_below_cimis_record_limit(action.payload.station_ids,
                                                        utils.parse_date_str(action.payload.start_date),
                                                        utils.parse_date_str(action.payload.end_date),
                                                        config.CIMIS_API_DAILY_RECORDS_PER_DAY):
                requests_as_list = utils.split_action(action)
                with ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
                    with client.get_queue_sender(config.SERVICE_BUS_RAW_QUEUE_NAME) as sender:
                        for new_action in requests_as_list:
                            new_msg = ServiceBusMessage(new_action.json())
                            sender.send_messages(new_msg)
                        logging.info(f'Split large message into smaller messages and sent to back of queue\
                            {config.SERVICE_BUS_RAW_QUEUE_NAME} at {utils.get_utc_timestamp()}')
            else:
                # Get cimis response
                cimis_response = DRDS.get_dailyraw_data_from_cimis(targets=action.payload.station_ids,
                                                                    start_date=utils.parse_date_str(action.payload.start_date),
                                                                    end_date=utils.parse_date_str(action.payload.end_date))
                logging.info(f'Received CIMIS response at {utils.get_utc_timestamp()}')
                rawdata_schema = DRDS.to_dailyraw_schema(cimis_response)
                DRDS.insert_dailyraw_data(rawdata_schema)
                logging.info(f'Successfully added data to dbo.DailyRaw at {utils.get_utc_timestamp()}')                                                                   

        else:
            # Discard message as it is the incorrect action type
            raise KeyError
                
    except (UnicodeDecodeError, ValueError, KeyError, OverflowError) as ERROR:
       # Treat unrecoverable errors as completed and log them
       logging.info('Unrecoverable error ' + str(ERROR) + f' at time {utils.get_utc_timestamp()}')

    except (ConnectionError, HTTPError, Timeout) as ERROR:
       with ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
           with client.get_queue_sender(config.SERVICE_BUS_RAW_QUEUE_NAME) as sender:
               # Update payload delivery count
               action.payload.delivery_count = action.payload.delivery_count + 1
               if action.payload.delivery_count < config.MAX_DELIVERY_COUNT:
                   # Get current time + exponential backoff based on delivery count to determine enqueue time
                   cur_time = datetime.datetime.utcnow()
                   delta_time = datetime.timedelta(seconds=1*(2**action.payload.delivery_count))
                   enqueue_time = cur_time + delta_time
                   # Create new message with same same payload as old message to allow modification
                   # Schedule enqueue time in new message constructor
                   new_msg = ServiceBusMessage(action.json(), scheduled_enqueue_time_utc=enqueue_time)
                   # Send message to queue
                   sender.send_messages(new_msg)
                   # Log sending message to queue
                   logging.info(f'Action {action} sent to back of queue \
                       {config.SERVICE_BUS_RAW_QUEUE_NAME} at {utils.get_utc_timestamp()}')
               else:
                   logging.info(f'Action {action} not requeued: max delivery count exceeded \
                       at {utils.get_utc_timestamp()}')

    except Exception as e:
       # Catch any unaccounted errors, log the time they occurred and payload leading
       # to the unaccounted error
       logging.info(f'Unaccounted error {e} thrown at time {utils.get_utc_timestamp()} from {action.json()}')

    
