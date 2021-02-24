# Azure functions
import azure.functions as func

# Debugging and logging
import logging
from requests import ConnectionError, HTTPError, Timeout

# Object management
import pydantic

# Shared objects
from shared.message import actions
from shared.stations.service import StationService

def main(msg: func.ServiceBusMessage):
    logging.info('station_message_queue_receiver ran at ')

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
            station_schema = StationService.to_station_schema(cimis_response)
            StationService.update_or_add_stations(station_schema)            

        elif action.action_type == actions.ActionType.STATIONS_UPDATE:
            # Update current list of stations
            action = pydantic.parse_raw_as(actions.AddStationsAction,
                                            message)
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
        