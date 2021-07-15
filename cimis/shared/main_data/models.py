from sqlalchemy import Column, Integer, Float, String, Date, Time

from shared.core.db import Base


class HourlyMainData(Base):
    __tablename__ = 'HourlyMain'

    Id = Column(Integer, primary_key=True, nullable=False)
    StationId = Column(Integer, nullable=False)
    Date = Column(Date, nullable=False)
    Hour = Column(Time, nullable=False)

    HlyAirTmp = Column(Float, nullable=True)
    HlyAirTmpUnits = Column(String(50), nullable=True, default='')

    HlyDewPnt = Column(Float, nullable=True)
    HlyDewPntUnits = Column(String(50), nullable=True, default='')

    HlyEto = Column(Float, nullable=True)
    HlyEtoUnits = Column(String(50), nullable=True, default='')

    HlyNetRad = Column(Float, nullable=True)
    HlyNetRadUnits = Column(String(50), nullable=True, default='')

    HlyAsceEto = Column(Float, nullable=True)
    HlyAsceEtoUnits = Column(String(50), nullable=True, default='')

    HlyAsceEtr = Column(Float, nullable=True)
    HlyAsceEtrUnits = Column(String(50), nullable=True, default='')

    HlyPrecip = Column(Float, nullable=True)
    HlyPrecipUnits = Column(String(50), nullable=True, default='')

    HlyRelHum = Column(Float, nullable=True)
    HlyRelHumUnits = Column(String(50), nullable=True, default='')

    HlyResWind = Column(Float, nullable=True)
    HlyResWindUnits = Column(String(50), nullable=True, default='')

    HlySoilTmp = Column(Float, nullable=True)
    HlySoilTmpUnits = Column(String(50), nullable=True, default='')

    HlySolRad = Column(Float, nullable=True)
    HlySolRadUnits = Column(String(50), nullable=True, default='')

    HlyVapPres = Column(Float, nullable=True)
    HlyVapPresUnits = Column(String(50), nullable=True, default='')

    HlyWindDir = Column(Float, nullable=True)
    HlyWindDirUnits = Column(String(50), nullable=True, default='')

    HlyWindSpd = Column(Float, nullable=True)
    HlyWindSpdUnits = Column(String(50), nullable=True, default='')


class DailyMainData(Base):
    __tablename__ = 'DailyMain'

    Id = Column(Integer, primary_key=True, nullable=False)
    StationId = Column(Integer, nullable=False)
    Date = Column(Date, nullable=False)

    DayAirTmpAvg = Column(Float, nullable=True)
    DayAirTmpAvgUnits = Column(String(50), nullable=True, default='')

    DayAirTmpMax = Column(Float, nullable=True)
    DayAirTmpMaxUnits = Column(String(50), nullable=True, default='')

    DayAirTmpMin = Column(Float, nullable=True)
    DayAirTmpMinUnits = Column(String(50), nullable=True, default='')

    DayDewPnt = Column(Float, nullable=True)
    DayDewPntUnits = Column(String(50), nullable=True, default='')

    DayEto = Column(Float, nullable=True)
    DayEtoUnits = Column(String(50), nullable=True, default='')

    DayAsceEto = Column(Float, nullable=True)
    DayAsceEtoUnits = Column(String(50), nullable=True, default='')

    DayAsceEtr = Column(Float, nullable=True)
    DayAsceEtrUnits = Column(String(50), nullable=True, default='')

    DayPrecip = Column(Float, nullable=True)
    DayPrecipUnits = Column(String(50), nullable=True, default='')

    DayRelHumAvg = Column(Float, nullable=True)
    DayRelHumAvgUnits = Column(String(50), nullable=True, default='')

    DayRelHumMax = Column(Float, nullable=True)
    DayRelHumMaxUnits = Column(String(50), nullable=True, default='')

    DayRelHumMin = Column(Float, nullable=True)
    DayRelHumMinUnits = Column(String(50), nullable=True, default='')

    DaySoilTmpAvg = Column(Float, nullable=True)
    DaySoilTmpAvgUnits = Column(String(50), nullable=True, default='')

    DaySoilTmpMax = Column(Float, nullable=True)
    DaySoilTmpMaxUnits = Column(String(50), nullable=True, default='')

    DaySoilTmpMin = Column(Float, nullable=True)
    DaySoilTmpMinUnits = Column(String(50), nullable=True, default='')

    DaySolRadAvg = Column(Float, nullable=True)
    DaySolRadAvgUnits = Column(String(50), nullable=True, default='')

    DaySolRadNet = Column(Float, nullable=True)
    DaySolRadNetUnits = Column(String(50), nullable=True, default='')

    DayVapPresAvg = Column(Float, nullable=True)
    DayVapPresAvgUnits = Column(String(50), nullable=True, default='')

    DayVapPresMax = Column(Float, nullable=True)
    DayVapPresMaxUnits = Column(String(50), nullable=True, default='')

    DayWindEne = Column(Float, nullable=True)
    DayWindEneUnits = Column(String(50), nullable=True, default='')

    DayWindEse = Column(Float, nullable=True)
    DayWindEseUnits = Column(String(50), nullable=True, default='')

    DayWindNne = Column(Float, nullable=True)
    DayWindNneUnits = Column(String(50), nullable=True, default='')

    DayWindNnw = Column(Float, nullable=True)
    DayWindNnwUnits = Column(String(50), nullable=True, default='')

    DayWindRun = Column(Float, nullable=True)
    DayWindRunUnits = Column(String(50), nullable=True, default='')

    DayWindSpdAvg = Column(Float, nullable=True)
    DayWindSpdAvgUnits = Column(String(50), nullable=True, default='')

    DayWindSsw = Column(Float, nullable=True)
    DayWindSswUnits = Column(String(50), nullable=True, default='')

    DayWindSse = Column(Float, nullable=True)
    DayWindSseUnits = Column(String(50), nullable=True, default='')

    DayWindWnw = Column(Float, nullable=True)
    DayWindWnwUnits = Column(String(50), nullable=True, default='')

    DayWindWsw = Column(Float, nullable=True)
    DayWindWswUnits = Column(String(50), nullable=True, default='')
