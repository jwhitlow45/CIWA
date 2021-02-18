from typing import List

import pydantic
import requests
import sqlalchemy
from shared import stations

from shared.stations import schemas
from shared.stations import models
from shared.core import config
from shared.core import db


class StationService:

    __base_url = 'http://et.water.ca.gov/api/station'

    @staticmethod
    def __parse_cimis_response(response: requests.Response) -> List[schemas.StationInCimisResponse]:
        """
        Args:
            response: The JSON reponse provided by the CIMIS API.
        Returns:
            List[schemas.StationInCimisResponse]: A list of StationRecord objects
                for each of the stations contained in the JSON reponse.
        Raises:
            ValueError: If the response body does not contain valid JSON.
            KeyError: If the JSON dictionary does not contain the expected properties.
        """
        json = response.json()
        stations = json['Stations']
        return pydantic.parse_obj_as(List[schemas.StationInCimisResponse], stations)

    @classmethod
    def get_stations_from_cimis(cls, targets: List[int] = None) -> List[schemas.StationInCimisResponse]:
        """Retrieves station info from the CIMIS API.

        Args:
            targets: If not None, returns info for only the target station ids.
                Otherwise, returns station info for all stations in CIMIS API.

        Returns:
            List[schemas.StationInCimisResponse]: List of StationRecord objects
                containing data and status info about the requests stations.

        Raises:
            ValueError: If the response body does not contain valid JSON.
            KeyError: If the JSON dictionary does not contain the expected properties.
            requests.ConnectionError: If a Connection error occurred.
            requests.HTTPError: If an HTTP error occurred.
            requests.Timeout: If the request timed out.
        """
        url = cls.__base_url

        # If the targets only contain 1 station, it's best to use the cimis api
        # endpoint for getting a single station by id.
        if targets and len(targets) == 1:
            url = f'{url}/{targets[0]}'

        response = requests.get(url, timeout=config.HTTP_TIMEOUT_SECONDS)
        response.raise_for_status()
        stations = cls.__parse_cimis_response(response)

        if targets:
            return [s for s in stations if s.StationNbr in targets]
        else:
            return stations

    @classmethod
    def get_stations_from_db(cls) -> List[schemas.Station]:
        """Retrieves station info from the database."""
        with db.session_manager() as session:
            stations = session.query(models.Station).order_by(models.Station.Id).all()
            return pydantic.parse_obj_as(List[schemas.Station], stations)

    @classmethod
    def update_or_add_station(cls, station: schemas.Station):
        """Adds or updates a station in the database.

        If the station already exists in the database, it will be updated.
        Otherwise, the staiton will be added to the database.
        """
        with db.session_manager() as session:
            session.merge(models.Station(**station.dict()))
            session.commit()

    @classmethod
    def batch_update_or_add_stations(cls, stations: List[schemas.Station]):
        """Same as update_or_add_stations but performs a batch operation."""
        with db.session_manager() as session:
            for station in stations:
                session.merge(models.Station(**station.dict()))
            session.commit()
