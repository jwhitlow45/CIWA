import logging

import azure.functions as func

import pydantic

from shared.message import actions
from shared.message import payloads
from shared.stations.service import StationService

def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    message = msg.get_body().decode('utf-8')
    action = pydantic.parse_obj_as(actions.Action, message)

    if action.action_type == actions.ActionType.STATIONS_ADD:
        action = pydantic.parse_obj_as(actions.AddStationsAction, message)
        # Add stations to list of stations
    elif action.action_type == actions.ActionType.STATIONS_UPDATE:
        action = pydantic.parse_obj_as(actions.AddStationsAction, message)
        # Update current list of stations
    else:
        # Discard message as it is the incorrect action type
        msg.dead_letter_source()
