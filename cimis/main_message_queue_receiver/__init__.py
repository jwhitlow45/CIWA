# Azure functions
from datetime import datetime
import azure.functions as func

# Debugging and logging
import logging

# Object parsing
import pydantic

# Shared objects
from shared.message import actions
from shared.main_data.service import MainDataService
from shared.core import config, utils

def main(msg: func.ServiceBusMessage):
    logging.info(f'raw_message_queue_receiver ran at {utils.get_utc_timestamp()}')
