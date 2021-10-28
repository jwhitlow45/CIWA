import datetime
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
    Month: int
    Day: int
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
                self.Month == other.Month,
                self.Day == other.Day,
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
    pass
