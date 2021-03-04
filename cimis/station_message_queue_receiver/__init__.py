# Azure functions
from datetime import datetime, timedelta
from os import utime
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
from shared.stations.service import StationService
from shared.core import config

def main(msg: func.ServiceBusMessage):
    utc_timestamp = datetime.datetime.utcnow()\
            .replace(tzinfo=datetime.timezone.utc)\
            .isoformat()
    logging.info(f'station_message_queue_receiver ran at {utc_timestamp}')

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
            logging.info(f'Received CIMIS reponse at {utc_timestamp}')
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)     
            logging.info(f'Succesfully added station(s) at {utc_timestamp}')       

        elif action.action_type == actions.ActionType.STATIONS_UPDATE:
            # Update current list of stations
            action = pydantic.parse_raw_as(actions.UpdateStationsAction,
                                            message)
            cimis_response = StationService.get_stations_from_cimis(action.payload.station_ids)
            logging.info(f'Received CIMIS reponse at {utc_timestamp}')
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)
            logging.info(f'Succesfully updated station(s) at {utc_timestamp}')       
            
        else:
            # Discard message as it is the incorrect action type
            raise KeyError
            
    except (UnicodeDecodeError, ValueError, KeyError) as ERROR:
        logging.info('Unrecoverable error ' + str(ERROR) + f' at time {utc_timestamp}')

    except (ConnectionError, HTTPError, Timeout) as ERROR:
        with ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
            with client.get_queue_sender(config.SERVICE_BUS_STATION_QUEUE_NAME) as sender:
                action.payload.delivery_count = action.payload.delivery_count + 1
                cur_time = datetime.datetime.utcnow()
                delta_time = datetime.timedelta(seconds=1*(2**action.payload.delivery_count))
                enqueue_time = cur_time + delta_time
                new_msg = ServiceBusMessage(action.json(), scheduled_enqueue_time_utc=enqueue_time)
                sender.send_messages(new_msg)
                logging.info('')
        