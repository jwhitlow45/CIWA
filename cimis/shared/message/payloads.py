from typing import List

import pydantic


class Payload(pydantic.BaseModel):
    class Config:
        extra = 'ignore'


class AddStationsPayload(Payload):
    station_ids: List[int]


class UpdateStationsPayload(Payload):
    station_ids: List[int]
