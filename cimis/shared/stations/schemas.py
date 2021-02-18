import datetime
from typing import Any, List, Optional

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

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, StationBase),
                self.Name == other.Name,
                self.City == other.City,
                self.RegionalOffice == other.RegionalOffice,
                self.County == other.County,
                self.IsActive == other.IsActive,
                self.IsEtoStation == other.IsEtoStation,
                self.Elevation == other.Elevation,
                self.GroundCover == other.GroundCover,
                self.SitingDesc == other.SitingDesc
            ]
        )


class StationInCimisResponse(StationBase):
    """Station info returned from the CIMIS API."""
    StationNbr: int
    ConnectDate: Optional[str]
    DisconnectDate: Optional[str]
    HmsLatitude: Optional[str]
    HmsLongitude: Optional[str]
    ZipCodes: Optional[List[str]]

    class Config:
        extra = 'ignore'

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, StationInCimisResponse),
                self.StationNbr == other.StationNbr,
                self.ConnectDate == other.ConnectDate,
                self.DisconnectDate == other.DisconnectDate,
                self.HmsLatitude == other.HmsLatitude,
                self.HmsLongitude == other.HmsLongitude,
            ]
        )


class Station(StationBase):
    """Station info stored in the database."""
    Id: int
    ConnectDate: Optional[datetime.date]
    DisconnectDate: Optional[datetime.date]
    Latitude: Optional[float]
    Longitude: Optional[float]

    class Config:
        extra = 'ignore'
        orm_mode = True

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                super().__eq__(other),
                isinstance(other, Station),
                self.Id == other.Id,
                self.ConnectDate == other.ConnectDate,
                self.DisconnectDate == other.DisconnectDate,
                self.Latitude == other.Latitude,
                self.Longitude == other.Longitude
            ]
        )
