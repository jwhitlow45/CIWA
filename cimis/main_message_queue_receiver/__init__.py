# Azure functions
import datetime
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
        raw_action = pydantic.parse_raw_as(actions.Action, message)
        logging.info(
            f'Message has been parsed successfully. ActionType: {action.action_type}')

        # Determine action type
        if action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
            action = pydantic.parse_raw_as(actions.CleanDailyRawDataAction,
                                           message)
            raw_action = pydantic.parse_raw_as(actions.CleanDailyRawDataAction,
                                               message)
            raw_action.action_type = actions.ActionType.DATA_ADD_DAILY_RAW
        elif action.action_type == actions.ActionType.DATA_CLEAN_HOURLY_RAW:
            action = pydantic.parse_raw_as(actions.CleanHourlyRawDataAction,
                                           message)
            raw_action = pydantic.parse_raw_as(actions.CleanHourlyRawDataAction,
                                               message)
            raw_action.action_type = actions.ActionType.DATA_ADD_HOURLY_RAW
        else:
            # Discard message as it is the incorrect action type
            raise TypeError('Invalid action type.')

        # Create DataServices with action
        MDS = MainDataService(action)
        RDS = RawDataService(raw_action)
        logging.info(
            f'Created DataServices with ActionTypes: {action.action_type} {raw_action.action_type}')

        # Parse action payload
        targets = action.payload.station_ids
        start_date = utils.parse_date_str(action.payload.start_date)
        end_date = utils.parse_date_str(action.payload.end_date)

        # Get raw and historical data
        raw_data = RDS.get_data_from_db(targets, start_date, end_date)
        historical_data = MDS.get_historical_data(
            targets, start_date, end_date)

        logging.info(f'Cleaning data for stations {targets}\
            from {start_date.strftime("%m/%d/%Y")}\
            to {end_date.strftime("%m/%d/%Y")}')
        cleaned_data = list(MDS.clean_data_from_db(
            raw_data, historical_data, RDS).values())
        logging.info(f'Cleaning data completed')
        MDS.insert_clean_data(cleaned_data)

    except Exception as e:
        # Catch any unaccounted errors, log the time they occurred and payload leading
        # to the unaccounted error
        logging.info(
            f'Unaccounted error {e} thrown at time {utils.get_utc_timestamp()} from {action.json()}')
        logging.info('Trace:\n' + traceback.format_exc())
