# Azure functions
from datetime import datetime
import azure.functions as func

# Debugging and logging
import logging
import traceback

# Object parsing
import pydantic

# Shared objects
from shared.message import actions
from shared.raw_data.service import RawDataService
from shared.main_data.service import MainDataService
from shared.core import config, utils


def main(msg: func.ServiceBusMessage):
    logging.info(
        f'raw_message_queue_receiver ran at {utils.get_utc_timestamp()}')

    try:
        # Store reponse in message string
        message = msg.get_body()
        logging.info(
            f'Received message from {config.SERVICE_BUS_MAIN_QUEUE_NAME}.')
        # Parse json message into Action object
        action = pydantic.parse_raw_as(actions.Action, message)
        logging.info(
            f'Message has been parsed successfully. ActionType: {action.action_type}')

        # Determine action type
        if action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
            action = pydantic.parse_raw_as(actions.CleanDailyRawDataAction,
                                           message)
        elif action.action_type == actions.ActionType.DATA_CLEAN_HOURLY_RAW:
            action = pydantic.parse_raw_as(actions.CleanHourlyRawDataAction,
                                           message)
        else:
            # Discard message as it is the incorrect action type
            raise TypeError('Invalid action type.')

        # Create DataServices with action
        RDS = RawDataService(action)
        MDS = MainDataService()
        logging.info(
            f'Created DataService with ActionType: {action.action_type}')

    except Exception as e:
        # Catch any unaccounted errors, log the time they occurred and payload leading
        # to the unaccounted error
        logging.info(
            f'Unaccounted error {e} thrown at time {utils.get_utc_timestamp()} from {action.json()}')
        logging.info('Trace:\n' + traceback.format_exc())
