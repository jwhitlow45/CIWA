import datetime
import logging

import azure.functions as func
import azure.servicebus as bus

from shared.core import config
from shared.message import actions
from shared.message import payloads
from shared.stations.service import StationService


def main(timer: func.TimerRequest) -> None:
    # Use UTC timestamp for logs
    utc_timestamp = datetime.datetime.utcnow()\
        .replace(tzinfo=datetime.timezone.utc)\
        .isoformat()

    # Log time to keep tabs on when each function ran.
    logging.info(f'daily_tick ran at {utc_timestamp}')

    stations = StationService.get_stations_from_db()
    station_ids = [s.Id for s in stations]

    with bus.ServiceBusClient.from_connection_string(config.SERVICE_BUS_CONNECTION_STRING) as client:
        # Send a message to update all station in the db to the station queue.
        with client.get_queue_sender(config.SERVICE_BUS_STATION_QUEUE_NAME) as sender:
            payload = payloads.UpdateStationsPayload(station_ids=station_ids)
            action = actions.UpdateStationsAction(payload=payload)
            message = bus.ServiceBusMessage(action.json())
            sender.send_messages(message)
