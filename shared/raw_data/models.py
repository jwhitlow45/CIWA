from sqlalchemy import Column, Integer, Float, String, Date, Time

from shared.core.db import Base


class HourlyRawData(Base):
    __tablename__ = 'HourlyRaw'

    Id = Column(Integer, primary_key=True, nullable=False)
    StationId = Column(Integer, nullable=False)
    Date = Column(Date, nullable=False)
    Hour = Column(Time, nullable=False)

    HlyAirTmp = Column(Float, nullable=True)
    HlyAirTmpQc = Column(String(50), nullable=True, default='')
    HlyAirTmpUnits = Column(String(50), nullable=True, default='')

    HlyDewPnt = Column(Float, nullable=True)
    HlyDewPntQc = Column(String(50), nullable=True, default='')
    HlyDewPntUnits = Column(String(50), nullable=True, default='')

    HlyEto = Column(Float, nullable=True)
    HlyEtoQc = Column(String(50), nullable=True, default='')
    HlyEtoUnits = Column(String(50), nullable=True, default='')

    HlyNetRad = Column(Float, nullable=True)
    HlyNetRadQc = Column(String(50), nullable=True, default='')
    HlyNetRadUnits = Column(String(50), nullable=True, default='')

    HlyAsceEto = Column(Float, nullable=True)
    HlyAsceEtoQc = Column(String(50), nullable=True, default='')
    HlyAsceEtoUnits = Column(String(50), nullable=True, default='')

    HlyAsceEtr = Column(Float, nullable=True)
    HlyAsceEtrQc = Column(String(50), nullable=True, default='')
    HlyAsceEtrUnits = Column(String(50), nullable=True, default='')

    HlyPrecip = Column(Float, nullable=True)
    HlyPrecipQc = Column(String(50), nullable=True, default='')
    HlyPrecipUnits = Column(String(50), nullable=True, default='')

    HlyRelHum = Column(Float, nullable=True)
    HlyRelHumQc = Column(String(50), nullable=True, default='')
    HlyRelHumUnits = Column(String(50), nullable=True, default='')

    HlyResWind = Column(Float, nullable=True)
    HlyResWindQc = Column(String(50), nullable=True, default='')
    HlyResWindUnits = Column(String(50), nullable=True, default='')

    HlySoilTmp = Column(Float, nullable=True)
    HlySoilTmpQc = Column(String(50), nullable=True, default='')
    HlySoilTmpUnits = Column(String(50), nullable=True, default='')

    HlySolRad = Column(Float, nullable=True)
    HlySolRadQc = Column(String(50), nullable=True, default='')
    HlySolRadUnits = Column(String(50), nullable=True, default='')

    HlyVapPres = Column(Float, nullable=True)
    HlyVapPresQc = Column(String(50), nullable=True, default='')
    HlyVapPresUnits = Column(String(50), nullable=True, default='')

    HlyWindDir = Column(Float, nullable=True)
    HlyWindDirQc = Column(String(50), nullable=True, default='')
    HlyWindDirUnits = Column(String(50), nullable=True, default='')

    HlyWindSpd = Column(Float, nullable=True)
    HlyWindSpdQc = Column(String(50), nullable=True, default='')
    HlyWindSpdUnits = Column(String(50), nullable=True, default='')


class DailyRawData(Base):
    __tablename__ = 'DailyRaw'

    Id = Column(Integer, primary_key=True, nullable=False)
    StationId = Column(Integer, nullable=False)
    Date = Column(Date, nullable=False)

    DayAirTmpAvg = Column(Float, nullable=True)
    DayAirTmpAvgQc = Column(String(50), nullable=True, default='')
    DayAirTmpAvgUnits = Column(String(50), nullable=True, default='')

    DayAirTmpMax = Column(Float, nullable=True)
    DayAirTmpMaxQc = Column(String(50), nullable=True, default='')
    DayAirTmpMaxUnits = Column(String(50), nullable=True, default='')

    DayAirTmpMin = Column(Float, nullable=True)
    DayAirTmpMinQc = Column(String(50), nullable=True, default='')
    DayAirTmpMinUnits = Column(String(50), nullable=True, default='')

    DayDewPnt = Column(Float, nullable=True)
    DayDewPntQc = Column(String(50), nullable=True, default='')
    DayDewPntUnits = Column(String(50), nullable=True, default='')

    DayEto = Column(Float, nullable=True)
    DayEtoQc = Column(String(50), nullable=True, default='')
    DayEtoUnits = Column(String(50), nullable=True, default='')

    DayAsceEto = Column(Float, nullable=True)
    DayAsceEtoQc = Column(String(50), nullable=True, default='')
    DayAsceEtoUnits = Column(String(50), nullable=True, default='')

    DayAsceEtr = Column(Float, nullable=True)
    DayAsceEtrQc = Column(String(50), nullable=True, default='')
    DayAsceEtrUnits = Column(String(50), nullable=True, default='')

    DayPrecip = Column(Float, nullable=True)
    DayPrecipQc = Column(String(50), nullable=True, default='')
    DayPrecipUnits = Column(String(50), nullable=True, default='')

    DayRelHumAvg = Column(Float, nullable=True)
    DayRelHumAvgQc = Column(String(50), nullable=True, default='')
    DayRelHumAvgUnits = Column(String(50), nullable=True, default='')

    DayRelHumMax = Column(Float, nullable=True)
    DayRelHumMaxQc = Column(String(50), nullable=True, default='')
    DayRelHumMaxUnits = Column(String(50), nullable=True, default='')

    DayRelHumMin = Column(Float, nullable=True)
    DayRelHumMinQc = Column(String(50), nullable=True, default='')
    DayRelHumMinUnits = Column(String(50), nullable=True, default='')

    DaySoilTmpAvg = Column(Float, nullable=True)
    DaySoilTmpAvgQc = Column(String(50), nullable=True, default='')
    DaySoilTmpAvgUnits = Column(String(50), nullable=True, default='')

    DaySoilTmpMax = Column(Float, nullable=True)
    DaySoilTmpMaxQc = Column(String(50), nullable=True, default='')
    DaySoilTmpMaxUnits = Column(String(50), nullable=True, default='')

    DaySoilTmpMin = Column(Float, nullable=True)
    DaySoilTmpMinQc = Column(String(50), nullable=True, default='')
    DaySoilTmpMinUnits = Column(String(50), nullable=True, default='')

    DaySolRadAvg = Column(Float, nullable=True)
    DaySolRadAvgQc = Column(String(50), nullable=True, default='')
    DaySolRadAvgUnits = Column(String(50), nullable=True, default='')

    DaySolRadNet = Column(Float, nullable=True)
    DaySolRadNetQc = Column(String(50), nullable=True, default='')
    DaySolRadNetUnits = Column(String(50), nullable=True, default='')

    DayVapPresAvg = Column(Float, nullable=True)
    DayVapPresAvgQc = Column(String(50), nullable=True, default='')
    DayVapPresAvgUnits = Column(String(50), nullable=True, default='')

    DayVapPresMax = Column(Float, nullable=True)
    DayVapPresMaxQc = Column(String(50), nullable=True, default='')
    DayVapPresMaxUnits = Column(String(50), nullable=True, default='')

    DayWindEne = Column(Float, nullable=True)
    DayWindEneQc = Column(String(50), nullable=True, default='')
    DayWindEneUnits = Column(String(50), nullable=True, default='')

    DayWindEse = Column(Float, nullable=True)
    DayWindEseQc = Column(String(50), nullable=True, default='')
    DayWindEseUnits = Column(String(50), nullable=True, default='')

    DayWindNne = Column(Float, nullable=True)
    DayWindNneQc = Column(String(50), nullable=True, default='')
    DayWindNneUnits = Column(String(50), nullable=True, default='')

    DayWindNnw = Column(Float, nullable=True)
    DayWindNnwQc = Column(String(50), nullable=True, default='')
    DayWindNnwUnits = Column(String(50), nullable=True, default='')

    DayWindRun = Column(Float, nullable=True)
    DayWindRunQc = Column(String(50), nullable=True, default='')
    DayWindRunUnits = Column(String(50), nullable=True, default='')

    DayWindSpdAvg = Column(Float, nullable=True)
    DayWindSpdAvgQc = Column(String(50), nullable=True, default='')
    DayWindSpdAvgUnits = Column(String(50), nullable=True, default='')

    DayWindSsw = Column(Float, nullable=True)
    DayWindSswQc = Column(String(50), nullable=True, default='')
    DayWindSswUnits = Column(String(50), nullable=True, default='')

    DayWindSse = Column(Float, nullable=True)
    DayWindSseQc = Column(String(50), nullable=True, default='')
    DayWindSseUnits = Column(String(50), nullable=True, default='')

    DayWindWnw = Column(Float, nullable=True)
    DayWindWnwQc = Column(String(50), nullable=True, default='')
    DayWindWnwUnits = Column(String(50), nullable=True, default='')

    DayWindWsw = Column(Float, nullable=True)
    DayWindWswQc = Column(String(50), nullable=True, default='')
    DayWindWswUnits = Column(String(50), nullable=True, default='')
