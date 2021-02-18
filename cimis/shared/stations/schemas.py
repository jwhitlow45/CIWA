import datetime
from typing import List, Optional

import pydantic


class StationBase(pydantic.BaseModel):
    Name: Optional[str]
    City: Optional[str]
    RegionalOffice: Optional[str]
    County: Optional[str]
    IsActive: Optional[bool]
    IsEtoStation: Optional[bool]
    Elevation: Optional[int]
    GroundCover: Optional[str]
    SitingDesc: Optional[str]

    class Config:
        extra = 'ignore'


class StationInCimisResponse(StationBase):
    """Station info returned from the CIMIS API."""
    StationNbr: int
    ConnectDate: Optional[str]
    DisconnectDate: Optional[str]
    HmsLatitude: Optional[str]
    HmsLongitude: Optional[str]
    ZipCodes: Optional[List[str]]


class Station(StationBase):
    """Station info stored in the database."""
    Id: int
    ConnectDate: Optional[datetime.date]
    DisconnectDate: Optional[datetime.date]
    Latitude: Optional[float]
    Longitude: Optional[float]

    class Config:
        orm_mode = True
