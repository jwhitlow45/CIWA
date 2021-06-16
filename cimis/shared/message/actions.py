from enum import Enum
from typing import Optional

import pydantic

from shared.message import payloads

class ActionType(str, Enum):
    STATIONS_ADD = 'stations/add'
    STATIONS_UPDATE = 'stations/update'
    DATA_GET_HOURLY_RAW = 'data/get_hourly_raw'
    DATA_GET_DAILY_RAW = 'data/get_daily_raw'


class Action(pydantic.BaseModel):
    action_type: ActionType
    payload: Optional[payloads.Payload]


class AddStationsAction(Action):
    action_type = ActionType.STATIONS_ADD
    payload: payloads.AddStationsPayload


class UpdateStationsAction(Action):
    action_type = ActionType.STATIONS_UPDATE
    payload: payloads.UpdateStationsPayload


class GetHourlyRawDataAction(Action):
    action_type = ActionType.DATA_GET_HOURLY_RAW
    payload: payloads.GetHourlyRawPayload


class GetDailyRawDataAction(Action):
    action_type = ActionType.DATA_GET_DAILY_RAW
    payload: payloads.GetDailyRawPayload