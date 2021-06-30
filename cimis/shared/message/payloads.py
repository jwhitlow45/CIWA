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


class AddHourlyRawPayload(Payload):
    station_ids: List[int]
    start_date: str
    end_date: str


class AddDailyRawPayload(Payload):
    station_ids: List[int]
    start_date: str
    end_date: str


class CleanHourlyRawPayload(Payload):
    station_ids: List[int]
    start_date: str
    end_date:str


class CleanDailyRawPayload(Payload):
    station_ids: List[int]
    start_date: str
    end_date:str