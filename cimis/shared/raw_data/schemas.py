import datetime
from typing import Any, List, Optional, Dict

import pydantic

# Hourly Raw Data Schemas
class HourlyRawBase(pydantic.BaseModel):
    
    Date: datetime.date
    Hour: datetime.time
    HlyAirTmp: dict
    HlyDewPnt: dict
    HlyEto: dict
    HlyNetRad: dict
    HlyAsceEto: dict
    HlyAsceEtr: dict
    HlyPrecip: dict
    HlyRelHum: dict
    HlyResWind: dict
    HlySoilTmp: dict
    HlySolRad: dict
    HlyVapPres: dict
    HlyWindDir: dict
    HlyWindSpd: dict

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

    Julian: int
    Station: int
    Standard: str
    ZipCodes: int
    Scope: str
    
    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, HourlyRawInCimisResponse),
                    self.Julian == other.Julian,
                    self.Station == other.Station,
                    self.Standard == other.Standard,
                    self.ZipCodes == other.ZipCodes,
                    self.Scope == other.Scope
            ]
        )


class HourlyRaw(HourlyRawBase):

    StationId: int

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, HourlyRaw),
                self.StationId == other.StationId
            ]
        )

# Daily Raw Data Schemas
class DailyRawBase(pydantic.BaseModel):

    Date: datetime.date
    DayAirTmpAvg: dict
    DayAirTmpMax: dict
    DayAirTmpMin: dict
    DayDewPnt: dict
    DayAsceEto: dict
    DayPrecip: dict
    DayRelHumAvg: dict
    DayRelHumMax: dict
    DayRelHumMin: dict
    DaySoilTmpAvg: dict
    DaySolRadAvg: dict
    DayVapPresAvg: dict
    DayWindRun: dict
    DayWindSpdAvg: dict

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

    Julian: int
    Station: int
    Standard: str
    ZipCodes: int
    Scope: str

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyRawInCimisResponse),
                self.Julian == other.Julian,
                self.Station == other.Station,
                self.Standard == other.Standard,
                self.ZipCodes == other.ZipCodes,
                self.Scope == other.Scope
            ]
        )

class DailyRaw(DailyRawBase):

    StationId: int

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyRaw),
                self.StationId == other.StationId
            ]
        )