from typing import List

import pydantic


class Payload(pydantic.BaseModel):
    class Config:
        extra = 'ignore'
    delivery_count: int    


class AddStationsPayload(Payload):
    station_ids: List[int]


class UpdateStationsPayload(Payload):
    station_ids: List[int]


class GetHourlyRawPayload(Payload):
    station_ids: List[int]
    start_date: str
    end_date: str


class GetDailyRawPayload(Payload):
    station_ids: List[int]
    start_date: str
    end_date: str
