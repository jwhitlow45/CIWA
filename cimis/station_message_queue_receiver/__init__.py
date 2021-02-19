# Azure functions
import azure.functions as func

# Debugging and logging
import logging
from requests import ConnectionError, HTTPError, Timeout

# Object management
import pydantic

# Response reading
import json

# Shared objects
from shared.message import actions
from shared.stations.service import StationService

def main(msg: func.ServiceBusMessage):
    logging.info('station_message_queue_receiver ran at ')

    try:
        # Store reponse in message string
        message = msg.get_body().decode('utf-8')
        # Convert message into json
        jsonMessage = json.loads(message)
        # Parse json message into Action object
        action = pydantic.parse_obj_as(actions.Action, jsonMessage)

        # NOTE: An action type of either STATIONS_ADD and STATIONS_UPDATE do the
        # same thing at this point in time. They were both added for
        # compatibility with future web applications.
        if action.action_type == actions.ActionType.STATIONS_ADD:
            # Add to list of stations
            action = pydantic.parse_obj_as(actions.AddStationsAction,
                                            jsonMessage)
            cimis_response = StationService.get_stations_from_cimis(action.payload.station_ids)
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)            

        elif action.action_type == actions.ActionType.STATIONS_UPDATE:
            # Update current list of stations
            action = pydantic.parse_obj_as(actions.AddStationsAction,
                                            jsonMessage)
            cimis_response = StationService.get_stations_from_cimis(action.payload.station_ids)
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)
            
        else:
            # Discard message as it is the incorrect action type
            pass
            
    except UnicodeDecodeError:
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
        logging.info('Request timed out')

"""Use shared.stations.service.StationService to get data for the requested station_ids in the payload from
CIMIS and update the db. You'll want to use
StationService.get_stations_from_cimis,
StationService.to_station_schema, and
StationService.update_or_add_stations for this"""

"""Read the docstrings for the functions. I list the types of exceptions that can be raised by them.
You'll want to use "try except" blocks so that you can determine weather to discard a message or abandon it to go back in the queue"""