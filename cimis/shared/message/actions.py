from enum import Enum
from typing import Optional

import pydantic

from shared.message import payloads

class ActionType(str, Enum):
    STATIONS_ADD = 'stations/add'
    STATIONS_UPDATE = 'stations/update'


class Action(pydantic.BaseModel):
    action_type: ActionType
    payload: Optional[payloads.Payload]


class AddStationsAction(Action):
    action_type = ActionType.STATIONS_ADD
    payload: payloads.AddStationsPayload


class UpdateStationsAction(Action):
    action_type = ActionType.STATIONS_UPDATE
    payload: payloads.UpdateStationsPayload
