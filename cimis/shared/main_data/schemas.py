from datetime import datetime
from typing import Any, Optional

import pydantic

# Daily Raw Data Schemas

class Sister(pydantic.BaseModel):

    class Config:
        extra = 'ignore'
    
    StationId: int
    FirstSisterId: int
    SecondSisterId: int

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, Sister)
            ]
        )

class HistoricalBase(pydantic.BaseModel):

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, HistoricalBase)
            ]
        )

class DailyHistorical(HistoricalBase):

    Id: int
    StationId: int
    Date: datetime.date
    Tmax: float
    Tmin: float
    AsceETo: float
    ETo: float
    Precip: float
    Rhmax: float
    Rhmin: float
    Wind: float

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyHistorical),
                self.Id == other.Id,
                self.StationId == other.StationId,
                self.Date == other.Date,
                self.Tmax == other.Tmax,
                self.Tmin == other.Tmin,
                self.AsceETo == other.AsceETo,
                self.ETo == other.ETo,
                self.Precip == other.Precip,
                self.Rhmax == other.Rhmax,
                self.Rhmin == other.Rhmin,
                self.Wind == other.Wind                
            ]
        )

class HourlyHistorical(HistoricalBase):

    Id: int 
    StationId: int 
    Date: datetime.date
    HlyAirTmp: float 
    HlyDewPnt: float 
    HlyPrecip: float 
    HlyRelHum: float 
    HlySoilTmp: float 
    HlyWindDir: float 
    HlyWindSpd: float 
    HlySolRad: float 
    HlyEto: float 
    HlyAsceEto: float

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, HourlyHistorical),
                self.Id == other.Id,
                self.StationId == other.StationId,
                self.Date == other.Date,
                self.HlyAirTmp == other.HlyAirTmp,
                self.HlyDewPnt == other.HlyDewPnt,
                self.HlyPrecip == other.HlyPrecip,
                self.HlyRelHum == other.HlyRelHum,
                self.HlySoilTmp == other.HlySoilTmp,
                self.HlyWindDir == other.HlyWindDir,
                self.HlyWindSpd == other.HlyWindSpd,
                self.HlySolRad == other.HlySolRad,
                self.HlyEto == other.HlyEto,
                self.HlyAsceEto == other.HlyAsceEto              
            ]
        )