# Azure functions
from datetime import datetime, timedelta
from os import utime
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import azure.functions as func

# Debugging and logging
import logging
import traceback
import datetime
from requests import ConnectionError, HTTPError, Timeout

# Type management
import pydantic

# Shared objects
from shared.message import actions
from shared.stations.service import StationService
from shared.core import config, utils

def main(msg: func.ServiceBusMessage):
    logging.info(f'station_message_queue_receiver ran at {utils.get_utc_timestamp()}')

    try:
        # Store reponse in message string
        message = msg.get_body()
        # Parse json message into Action object
        action = pydantic.parse_raw_as(actions.Action, message)

        # NOTE: An action type of either STATIONS_ADD and STATIONS_UPDATE do the
        # same thing at this point in time. They were both added for
        # compatibility with future web applications.
        if action.action_type == actions.ActionType.STATIONS_ADD:
            # Add to list of stations
            action = pydantic.parse_raw_as(actions.AddStationsAction,
                                            message)
            cimis_response = StationService.get_stations_from_cimis(action.payload.station_ids)
            logging.info(f'Received CIMIS reponse at {utils.get_utc_timestamp()}')
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)     
            logging.info(f'Succesfully added station(s) at {utils.get_utc_timestamp()}')       

        elif action.action_type == actions.ActionType.STATIONS_UPDATE:
            # Update current list of stations
            action = pydantic.parse_raw_as(actions.UpdateStationsAction,
                                            message)
            cimis_response = StationService.get_stations_from_cimis(action.payload.station_ids)
            logging.info(f'Received CIMIS reponse at {utils.get_utc_timestamp()}')
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)
            logging.info(f'Succesfully updated station(s) at {utils.get_utc_timestamp()}')       
            
        else:
            # Discard message as it is the incorrect action type
            raise KeyError
            
    except (UnicodeDecodeError, ValueError, KeyError) as ERROR:
        # Treat unrecoverable errors as completed and log them
        logging.info('Unrecoverable error ' + str(ERROR) + f' at time {utils.get_utc_timestamp()}')
        logging.info('Trace:\n' + traceback.format_exc())

    except (ConnectionError, HTTPError, Timeout) as ERROR:
        with ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
            with client.get_queue_sender(config.SERVICE_BUS_STATION_QUEUE_NAME) as sender:
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
                        {config.SERVICE_BUS_STATION_QUEUE_NAME} at {utils.get_utc_timestamp()}')
                else:
                    logging.info(f'Action {action} not requeued: max delivery count exceeded \
                        at {utils.get_utc_timestamp()}')

    except Exception as e:
        # Catch any unaccounted errors, log the time they occurred and payload leading
        # to the unaccounted error
        logging.info(f'Unaccounted error {e} thrown at time {utils.get_utc_timestamp()} from {action.json()}')
        logging.info('Trace:\n' + traceback.format_exc())