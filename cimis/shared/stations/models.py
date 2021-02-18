from sqlalchemy import Column, Integer, Float, String, Text, Boolean, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from shared.core.db import Base

class Station(Base):
    __tablename__ = 'Station'

    Id = Column(Integer, primary_key=True, autoincrement=False)
    Name = Column(String(255), nullable=True, default='')
    City = Column(String(255), nullable=True, default='')
    RegionalOffice = Column(String(255), nullable=True, default='')
    County = Column(String(255), nullable=True, default='')
    ConnectDate = Column(Date, nullable=True)
    DisconnectDate = Column(Date, nullable=True)
    IsActive = Column(Boolean, nullable=True, default=False)
    IsEtoStation = Column(Boolean, nullable=True, default=False)
    Elevation = Column(Integer, nullable=True)
    GroundCover = Column(String(255), nullable=True, default='')
    Latitude = Column(Float, nullable=True)
    Longitude = Column(Float, nullable=True)
    SitingDesc = Column(Text, nullable=True, default='')
