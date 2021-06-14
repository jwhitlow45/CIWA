import datetime
from typing import Any, List, Optional

import pydantic

class HourlyRawBase(pydantic.BaseModel):
    
    Date: datetime.date
    Hour: datetime.time
    HlyAirTemp = Optional[dict]
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
                self.HlyAirTemp == other.HlyAirTemp,
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

