from enum import Enum
from typing import Optional

import pydantic

from shared.message import payloads

class ActionType(str, Enum):
    STATIONS_ADD = 'stations/add'
    STATIONS_UPDATE = 'stations/update'
    DATA_ADD_HOURLY_RAW = 'data/add_hourly_raw'
    DATA_ADD_DAILY_RAW = 'data/add_daily_raw'


class Action(pydantic.BaseModel):
    action_type: ActionType
    payload: Optional[payloads.Payload]


class AddStationsAction(Action):
    action_type = ActionType.STATIONS_ADD
    payload: payloads.AddStationsPayload


class UpdateStationsAction(Action):
    action_type = ActionType.STATIONS_UPDATE
    payload: payloads.UpdateStationsPayload


class AddHourlyRawDataAction(Action):
    action_type = ActionType.DATA_ADD_HOURLY_RAW
    payload: payloads.GetHourlyRawPayload


class AddDailyRawDataAction(Action):
    action_type = ActionType.DATA_ADD_DAILY_RAW
    payload: payloads.GetDailyRawPayload