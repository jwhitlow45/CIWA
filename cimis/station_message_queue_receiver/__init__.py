# Azure functions
from datetime import datetime
from os import utime
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import azure.functions as func

# Debugging and logging
import logging
import datetime
from requests import ConnectionError, HTTPError, Timeout

# Type management
import pydantic
import json

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
        pass

    except (ConnectionError, HTTPError, Timeout) as ERROR:
        with ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
            with client.get_queue_sender(config.SERVICE_BUS_STATION_QUEUE_NAME) as sender:
                action.payload.delivery_count = action.payload.delivery_count + 1
                new_msg = ServiceBusMessage()
                new_msg.scheduled_enqueue_time_utc(seconds=1*(2**action.payload.delivery_count))
                sender.send_messages(action)


""" UnicodeDecodeError:
        logging.info('Message received in unreadable format')
    except ValueError:
        logging.info('Response does not contain valid JSON')
    except KeyError:
        logging.info('JSON dictionary does not contain expected properties')
    except ConnectionError:
        logging.info('Connection error occured')
    except HTTPError:
        logging.info('HTTP error occured')
    except Timeout:
        logging.info('Request timed out')"""
        