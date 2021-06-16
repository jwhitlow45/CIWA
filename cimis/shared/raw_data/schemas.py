import datetime
from typing import Any, List, Optional

import pydantic

# Hourly Raw Data Schemas
class HourlyRawBase(pydantic.BaseModel):
    
    Date: datetime.date
    Hour: datetime.time
    HlyAirTmp = Optional[dict]
    HlyDewPnt = Optional[dict]
    HlyEto = Optional[dict]
    HlyNetRad = Optional[dict]
    HlyAsceEto = Optional[dict]
    HlyAsceEtr = Optional[dict]
    HlyPrecip = Optional[dict]
    HlyRelHum = Optional[dict]
    HlyResWind = Optional[dict]
    HlySoilTmp = Optional[dict]
    HlySolRad = Optional[dict]
    HlyVapPres = Optional[dict]
    HlyWindDir = Optional[dict]
    HlyWindSpd = Optional[dict]

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, HourlyRawBase),
                self.Date == other.Date ,
                self.Hour == other.Hour,
                self.HlyAirTmp == other.HlyAirTmp,
                self.HlyDewPnt == other.HlyDewPnt,
                self.HlyEto == other.HlyEto,
                self.HlyNetRad == other.HlyNetRad,
                self.HlyAsceEto == other.HlyAsceEto,
                self.HlyAsceEtr == other.HlyAsceEtr,
                self.HlyPrecip == other.HlyPrecip,
                self.HlyRelHum == other.HlyRelHum,
                self.HlyResWind == other.HlyResWind,
                self.HlySoilTmp == other.HlySoilTmp,
                self.HlySolRad == other.HlySolRad,
                self.HlyVapPres == other.HlyVapPres,
                self.HlyWindDir == other.HlyWindDir,
                self.HlyWindSpd == other.HlyWindSpd
            ]
        )

class HourlyRawInCimisResponse(HourlyRawBase):

    Station: int
    
    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, HourlyRawInCimisResponse),
                self.Station == other.Station
            ]
        )


class HourlyRaw(HourlyRawBase):

    Id: int
    StationId: int

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, HourlyRaw),
                self.Id == other.Id
            ]
        )

# Daily Raw Data Schemas
class DailyRawBase(pydantic.BaseModel):

    Date: datetime.date
    DayAirTmpAvg: Optional[dict]
    DayAirTmpMax: Optional[dict]
    DayAirTmpMin: Optional[dict]
    DayDewPnt: Optional[dict]
    DayAsceEto: Optional[dict]
    DayPrecip: Optional[dict]
    DayRelHumAvg: Optional[dict]
    DayRelHumMax: Optional[dict]
    DayRelHumMin: Optional[dict]
    DaySoilTmpAvg: Optional[dict]
    DaySolRadAvg: Optional[dict]
    DayVapPresAvg: Optional[dict]
    DayWindRun: Optional[dict]
    DayWindSpdAvg: Optional[dict]

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, DailyRawBase),
                self.Date == other.Date,
                self.DayAirTmpAvg == other.DayAirTmpAvg,
                self.DayAirTmpMax == other.DayAirTmpMax,
                self.DayAirTmpMin == other.DayAirTmpMin,
                self.DayDewPnt == other.DayDewPnt,
                self.DayAsceEto == other.DayAsceEto,
                self.DayPrecip == other.DayPrecip,
                self.DayRelHumAvg == other.DayRelHumAvg,
                self.DayRelHumMax == other.DayRelHumMax,
                self.DayRelHumMin == other.DayRelHumMin,
                self.DaySoilTmpAvg == other.DaySoilTmpAvg,
                self.DaySolRadAvg == other.DaySolRadAvg,
                self.DayVapPresAvg == other.DayVapPresAvg,
                self.DayWindRun == other.DayWindRun,
                self.DayWindSpdAvg == other.DayWindSpdAvg
            ]
        )

class DailyRawInCimisResponse(DailyRawBase):

    Station: int

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyRawInCimisResponse),
                self.Station == other.Station
            ]
        )

class DailyRaw(DailyRawBase):

    Id: int
    StationId: int

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyRaw),
                self.Id == other.Id
            ]
        )