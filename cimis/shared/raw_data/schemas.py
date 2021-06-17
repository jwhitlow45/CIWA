import datetime
from typing import Any, Optional

import pydantic

# Hourly Raw Data Schemas
class HourlyRawBase(pydantic.BaseModel):
    

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, HourlyRawBase)
            ]
        )

class HourlyRawInCimisResponse(HourlyRawBase):

    Date: str
    Hour: str
    Julian: Optional[int]
    Station: Optional[int]
    Standard: Optional[str]
    ZipCodes: Optional[str]
    Scope: Optional[str]
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
                super().__eq__(other),
                isinstance(other, HourlyRawInCimisResponse),
                    self.Date == other.Date,
                    self.Hour == other.Hour,
                    self.Julian == other.Julian,
                    self.Station == other.Station,
                    self.Standard == other.Standard,
                    self.ZipCodes == other.ZipCodes,
                    self.Scope == other.Scope,
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

class HourlyRaw(HourlyRawBase):

    Id: str
    StationId: int
    Date: datetime.date
    Hour: datetime.time

    HlyAirTmp: Optional[float]
    HlyAirTmpQc: Optional[str]
    HlyAirTmpUnits: Optional[str]

    HlyDewPnt: Optional[float]
    HlyDewPntQc: Optional[str]
    HlyDewPntUnits: Optional[str]

    HlyEto: Optional[float]
    HlyEtoQc: Optional[str]
    HlyEtoUnits: Optional[str]

    HlyNetRad: Optional[float]
    HlyNetRadQc: Optional[str]
    HlyNetRadUnits: Optional[str]

    HlyAsceEto: Optional[float]
    HlyAsceEtoQc: Optional[str]
    HlyAsceEtoUnits: Optional[str]

    HlyAsceEtr: Optional[float]
    HlyAsceEtrQc: Optional[str]
    HlyAsceEtrUnits: Optional[str]

    HlyPrecip: Optional[float]
    HlyPrecipQc: Optional[str]
    HlyPrecipUnits: Optional[str]

    HlyRelHum: Optional[float]
    HlyRelHumQc: Optional[str]
    HlyRelHumUnits: Optional[str]

    HlyResWind: Optional[float]
    HlyResWindQc: Optional[str]
    HlyResWindUnits: Optional[str]

    HlySoilTmp: Optional[float]
    HlySoilTmpQc: Optional[str]
    HlySoilTmpUnits: Optional[str]

    HlySolRad: Optional[float]
    HlySolRadQc: Optional[str]
    HlySolRadUnits: Optional[str]

    HlyVapPres: Optional[float]
    HlyVapPresQc: Optional[str]
    HlyVapPresUnits: Optional[str]

    HlyWindDir: Optional[float]
    HlyWindDirQc: Optional[str]
    HlyWindDirUnits: Optional[str]

    HlyWindSpd: Optional[float]
    HlyWindSpdQc: Optional[str]
    HlyWindSpdUnits: Optional[str]

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, HourlyRaw),
                self.Id == other.Id,
                self.StationId == other.StationId,
                self.Date == other.Date,
                self.Hour == other.Hour,                
                self.HlyAirTmp == other.HlyAirTmp,
                self.HlyAirTmpQc == other.HlyAirTmpQc,
                self.HlyAirTmpUnits == other.HlyAirTmpUnits,
                self.HlyDewPnt == other.HlyDewPnt,
                self.HlyDewPntQc == other.HlyDewPntQc,
                self.HlyDewPntUnits == other.HlyDewPntUnits,
                self.HlyEto == other.HlyEto,
                self.HlyEtoQc == other.HlyEtoQc,
                self.HlyEtoUnits == other.HlyEtoUnits,
                self.HlyNetRad == other.HlyNetRad,
                self.HlyNetRadQc == other.HlyNetRadQc,
                self.HlyNetRadUnits == other.HlyNetRadUnits,
                self.HlyAsceEto == other.HlyAsceEto,
                self.HlyAsceEtoQc == other.HlyAsceEtoQc,
                self.HlyAsceEtoUnits == other.HlyAsceEtoUnits,
                self.HlyAsceEtr == other.HlyAsceEtr,
                self.HlyAsceEtrQc == other.HlyAsceEtrQc,
                self.HlyAsceEtrUnits == other.HlyAsceEtrUnits,
                self.HlyPrecip == other.HlyPrecip,
                self.HlyPrecipQc == other.HlyPrecipQc,
                self.HlyPrecipUnits == other.HlyPrecipUnits,
                self.HlyRelHum == other.HlyRelHum,
                self.HlyRelHumQc == other.HlyRelHumQc,
                self.HlyRelHumUnits == other.HlyRelHumUnits,
                self.HlyResWind == other.HlyResWind,
                self.HlyResWindQc == other.HlyResWindQc,
                self.HlyResWindUnits == other.HlyResWindUnits,
                self.HlySoilTmp == other.HlySoilTmp,
                self.HlySoilTmpQc == other.HlySoilTmpQc,
                self.HlySoilTmpUnits == other.HlySoilTmpUnits,
                self.HlySolRad == other.HlySolRad,
                self.HlySolRadQc == other.HlySolRadQc,
                self.HlySolRadUnits == other.HlySolRadUnits,
                self.HlyVapPres == other.HlyVapPres,
                self.HlyVapPresQc == other.HlyVapPresQc,
                self.HlyVapPresUnits == other.HlyVapPresUnits,
                self.HlyWindDir == other.HlyWindDir,
                self.HlyWindDirQc == other.HlyWindDirQc,
                self.HlyWindDirUnits == other.HlyWindDirUnits,
                self.HlyWindSpd == other.HlyWindSpd,
                self.HlyWindSpdQc == other.HlyWindSpdQc,
                self.HlyWindSpdUnits == other.HlyWindSpdUnits
            ]
        )

# Daily Raw Data Schemas
class DailyRawBase(pydantic.BaseModel):

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, DailyRawBase)
            ]
        )

class DailyRawInCimisResponse(DailyRawBase):

    Date: str
    Julian: int
    Station: int
    Standard: str
    ZipCodes: str
    Scope: str
    DayAirTmpAvg: dict
    DayAirTmpMax: dict
    DayAirTmpMin: dict
    DayDewPnt: dict
    DayEto: dict
    DayAsceEto: dict
    DayAsceEtr: dict
    DayPrecip: dict
    DayRelHumAvg: dict
    DayRelHumMax: dict
    DayRelHumMin: dict
    DaySoilTmpAvg: dict
    DaySoilTmpMax: dict
    DaySoilTmpMin: dict
    DaySolRadAvg: dict
    DaySolRadNet: dict
    DayVapPresAvg: dict
    DayVapPresMax: dict
    DayWindEne: dict
    DayWindEse: dict
    DayWindNne: dict
    DayWindNnw: dict
    DayWindRun: dict
    DayWindSsw: dict
    DayWindWnw: dict
    DayWindWsw: dict

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyRawInCimisResponse),
                self.Date == other.Date,
                self.Julian == other.Julian,
                self.Station == other.Station,
                self.Standard == other.Standard,
                self.ZipCodes == other.ZipCodes,
                self.Scope == other.Scope,
                self.DayAirTmpAvg == other.DayAirTmpAvg,
                self.DayAirTmpMax == other.DayAirTmpMax,
                self.DayAirTmpMin == other.DayAirTmpMin,
                self.DayDewPnt == other.DayDewPnt,
                self.DayEto == other.DayEto,
                self.DayAsceEto == other.DayAsceEto,
                self.DayAsceEtr == other.DayAsceEtr,
                self.DayPrecip == other.DayPrecip,
                self.DayRelHumAvg == other.DayRelHumAvg,
                self.DayRelHumMax == other.DayRelHumMax,
                self.DayRelHumMin == other.DayRelHumMin,
                self.DaySoilTmpAvg == other.DaySoilTmpAvg,
                self.DaySoilTmpMax == other.DaySoilTmpMax,
                self.DaySoilTmpMin == other.DaySoilTmpMin,
                self.DaySolRadAvg == other.DaySolRadAvg,
                self.DaySolRadNet == other.DaySolRadNet,
                self.DayVapPresAvg == other.DayVapPresAvg,
                self.DayVapPresMax == other.DayVapPresMax,
                self.DayWindEne == other.DayWindEne,
                self.DayWindEse == other.DayWindEse,
                self.DayWindNne == other.DayWindNne,
                self.DayWindNnw == other.DayWindNnw,
                self.DayWindRun == other.DayWindRun,
                self.DayWindSsw == other.DayWindSsw,
                self.DayWindWnw == other.DayWindWnw,
                self.DayWindWsw == other.DayWindWsw
            ]
        )

class DailyRaw(DailyRawBase):

    Id: str
    StationId: int
    Date: datetime.date
    
    DayAirTmpAvg: Optional[float]
    DayAirTmpAvgQc: Optional[str]
    DayAirTmpAvgUnits: Optional[str]

    DayAirTmpMax: Optional[float]
    DayAirTmpMaxQc: Optional[str]
    DayAirTmpMaxUnits: Optional[str]

    DayAirTmpMin: Optional[float]
    DayAirTmpMinQc: Optional[str]
    DayAirTmpMinUnits: Optional[str]

    DayDewPnt: Optional[float]
    DayDewPntQc: Optional[str]
    DayDewPntUnits: Optional[str]

    DayEto: Optional[float]
    DayEtoQc: Optional[str]
    DayEtoUnits: Optional[str]

    DayAsceEto: Optional[float]
    DayAsceEtoQc: Optional[str]
    DayAsceEtoUnits: Optional[str]

    DayAsceEtr: Optional[float]
    DayAsceEtrQc: Optional[str]
    DayAsceEtrUnits: Optional[str]

    DayPrecip: Optional[float]
    DayPrecipQc: Optional[str]
    DayPrecipUnits: Optional[str]

    DayRelHumAvg: Optional[float]
    DayRelHumAvgQc: Optional[str]
    DayRelHumAvgUnits: Optional[str]

    DayRelHumMax: Optional[float]
    DayRelHumMaxQc: Optional[str]
    DayRelHumMaxUnits: Optional[str]

    DayRelHumMin: Optional[float]
    DayRelHumMinQc: Optional[str]
    DayRelHumMinUnits: Optional[str]

    DaySoilTmpAvg: Optional[float]
    DaySoilTmpAvgQc: Optional[str]
    DaySoilTmpAvgUnits: Optional[str]

    DaySoilTmpMax: Optional[float]
    DaySoilTmpMaxQc: Optional[str]
    DaySoilTmpMaxUnits: Optional[str]

    DaySoilTmpMin: Optional[float]
    DaySoilTmpMinQc: Optional[str]
    DaySoilTmpMinUnits: Optional[str]

    DaySolRadAvg: Optional[float]
    DaySolRadAvgQc: Optional[str]
    DaySolRadAvgUnits: Optional[str]

    DaySolRadNet: Optional[float]
    DaySolRadNetQc: Optional[str]
    DaySolRadNetUnits: Optional[str]

    DayVapPresAvg: Optional[float]
    DayVapPresAvgQc: Optional[str]
    DayVapPresAvgUnits: Optional[str]

    DayVapPresMax: Optional[float]
    DayVapPresMaxQc: Optional[str]
    DayVapPresMaxUnits: Optional[str]

    DayWindEne: Optional[float]
    DayWindEneQc: Optional[str]
    DayWindEneUnits: Optional[str]

    DayWindEse: Optional[float]
    DayWindEseQc: Optional[str]
    DayWindEseUnits: Optional[str]

    DayWindNne: Optional[float]
    DayWindNneQc: Optional[str]
    DayWindNneUnits: Optional[str]

    DayWindNnw: Optional[float]
    DayWindNnwQc: Optional[str]
    DayWindNnwUnits: Optional[str]

    DayWindRun: Optional[float]
    DayWindRunQc: Optional[str]
    DayWindRunUnits: Optional[str]

    DayWindSsw: Optional[float]
    DayWindSswQc: Optional[str]
    DayWindSswUnits: Optional[str]

    DayWindWnw: Optional[float]
    DayWindWnwQc: Optional[str]
    DayWindWnwUnits: Optional[str]

    DayWindWsw: Optional[float]
    DayWindWswQc: Optional[str]
    DayWindWswUnits: Optional[str]
    

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, DailyRaw),
                self.Id == other.Id,
                self.Date == other.Date,
                self.StationId == other.StationId,
                self.DayAirTmpAvg == other.DayAirTmpAvg,
                self.DayAirTmpAvgQc == other.DayAirTmpAvgQc,
                self.DayAirTmpAvgUnits == other.DayAirTmpAvgUnits,
                self.DayAirTmpMax == other.DayAirTmpMax,
                self.DayAirTmpMaxQc == other.DayAirTmpMaxQc,
                self.DayAirTmpMaxUnits == other.DayAirTmpMaxUnits,
                self.DayAirTmpMin == other.DayAirTmpMin,
                self.DayAirTmpMinQc == other.DayAirTmpMinQc,
                self.DayAirTmpMinUnits == other.DayAirTmpMinUnits,
                self.DayDewPnt == other.DayDewPnt,
                self.DayDewPntQc == other.DayDewPntQc,
                self.DayDewPntUnits == other.DayDewPntUnits,
                self.DayEto == other.DayEto,
                self.DayEtoQc == other.DayEtoQc,
                self.DayEtoUnits == other.DayEtoUnits,
                self.DayAsceEto == other.DayAsceEto,
                self.DayAsceEtoQc == other.DayAsceEtoQc,
                self.DayAsceEtoUnits == other.DayAsceEtoUnits,
                self.DayAsceEtr == other.DayAsceEtr,
                self.DayAsceEtrQc == other.DayAsceEtrQc,
                self.DayAsceEtrUnits == other.DayAsceEtrUnits,
                self.DayPrecip == other.DayPrecip,
                self.DayPrecipQc == other.DayPrecipQc,
                self.DayPrecipUnits == other.DayPrecipUnits,
                self.DayRelHumAvg == other.DayRelHumAvg,
                self.DayRelHumAvgQc == other.DayRelHumAvgQc,
                self.DayRelHumAvgUnits == other.DayRelHumAvgUnits,
                self.DayRelHumMax == other.DayRelHumMax,
                self.DayRelHumMaxQc == other.DayRelHumMaxQc,
                self.DayRelHumMaxUnits == other.DayRelHumMaxUnits,
                self.DayRelHumMin == other.DayRelHumMin,
                self.DayRelHumMinQc == other.DayRelHumMinQc,
                self.DayRelHumMinUnits == other.DayRelHumMinUnits,
                self.DaySoilTmpAvg == other.DaySoilTmpAvg,
                self.DaySoilTmpAvgQc == other.DaySoilTmpAvgQc,
                self.DaySoilTmpAvgUnits == other.DaySoilTmpAvgUnits,
                self.DaySoilTmpMax == other.DaySoilTmpMax,
                self.DaySoilTmpMaxQc == other.DaySoilTmpMaxQc,
                self.DaySoilTmpMaxUnits == other.DaySoilTmpMaxUnits,
                self.DaySoilTmpMin == other.DaySoilTmpMin,
                self.DaySoilTmpMinQc == other.DaySoilTmpMinQc,
                self.DaySoilTmpMinUnits == other.DaySoilTmpMinUnits,
                self.DaySolRadAvg == other.DaySolRadAvg,
                self.DaySolRadAvgQc == other.DaySolRadAvgQc,
                self.DaySolRadAvgUnits == other.DaySolRadAvgUnits,
                self.DaySolRadNet == other.DaySolRadNet,
                self.DaySolRadNetQc == other.DaySolRadNetQc,
                self.DaySolRadNetUnits == other.DaySolRadNetUnits,
                self.DayVapPresAvg == other.DayVapPresAvg,
                self.DayVapPresAvgQc == other.DayVapPresAvgQc,
                self.DayVapPresAvgUnits == other.DayVapPresAvgUnits,
                self.DayVapPresMax == other.DayVapPresMax,
                self.DayVapPresMaxQc == other.DayVapPresMaxQc,
                self.DayVapPresMaxUnits == other.DayVapPresMaxUnits,
                self.DayWindEne == other.DayWindEne,
                self.DayWindEneQc == other.DayWindEneQc,
                self.DayWindEneUnits == other.DayWindEneUnits,
                self.DayWindEse == other.DayWindEse,
                self.DayWindEseQc == other.DayWindEseQc,
                self.DayWindEseUnits == other.DayWindEseUnits,
                self.DayWindNne == other.DayWindNne,
                self.DayWindNneQc == other.DayWindNneQc,
                self.DayWindNneUnits == other.DayWindNneUnits,
                self.DayWindNnw == other.DayWindNnw,
                self.DayWindNnwQc == other.DayWindNnwQc,
                self.DayWindNnwUnits == other.DayWindNnwUnits,
                self.DayWindRun == other.DayWindRun,
                self.DayWindRunQc == other.DayWindRunQc,
                self.DayWindRunUnits == other.DayWindRunUnits,
                self.DayWindSsw == other.DayWindSsw,
                self.DayWindSswQc == other.DayWindSswQc,
                self.DayWindSswUnits == other.DayWindSswUnits,
                self.DayWindWnw == other.DayWindWnw,
                self.DayWindWnwQc == other.DayWindWnwQc,
                self.DayWindWnwUnits == other.DayWindWnwUnits,
                self.DayWindWsw == other.DayWindWsw,
                self.DayWindWswQc == other.DayWindWswQc,
                self.DayWindWswUnits == other.DayWindWswUnits
            ]
        )