from typing import List
from datetime import date
import pydantic
import requests

import os

from sqlalchemy.sql.sqltypes import Date

from shared.core import config
from shared.core import db
from shared.core import utils
from shared.raw_data import schemas

class HourlyRawDataService():

    __base_url = config.CIMIS_API_DATA_BASE_URL

    __data_items = [
        "hly-air-tmp",
        "hly-dew-pnt",
        "hly-eto",
        "hly-net-rad",
        "hly-asce-eto",
        "hly-asce-etr",
        "hly-precip",
        "hly-rel-hum",
        "hly-res-wind",
        "hly-soil-tmp",
        "hly-sol-rad",
        "hly-vap-pres",
        "hly-wind-dir",
        "hly-wind-spd"
    ]

    # -------------------------------------------------------------------------
    # Private helper methods
    # -------------------------------------------------------------------------
    @staticmethod
    def __parse_cimis_response(reponse: requests.Response) -> List[schemas.HourlyRawInCimisResponse]:
        """
        Args:
            reponse: The JSON response provided by the CIMIS API.
        Returns:
            List[schemas.HourlyRawInCimisResponse]: A list of HourlyRecord objects
            for each hour of each station in the JSON response
        Raises:
            ValueError: If the response body does not contain valid JSON.
            KeyError: If the JSON dictionary does not contain the expected properties.
        """

        pass

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------
    @classmethod
    def to_hourlyraw_schema(cls, stations: List[schemas.HourlyRawInCimisResponse]) -> List[schemas.HourlyRaw]:
        """Converts hourlyraw schema from HourlyRawInCimisResponse to HourlyRaw"""
        pass

    @classmethod
    def get_hourlyraw_data_from_cimis(cls, startDate: date, endDate: date, targets: List[int] = None) -> List[schemas.HourlyRawInCimisResponse]:
        """Retrieves hourly raw data from CIMIS API.

        Args:
            startDate: Date from which data will start to be gathered
            endDate: Date to which data will stop being gathered
            targets: If not None, returns hourly raw data for only the target station ids.
                    Otherwise, returns hourly raw data for all stations in CIMIS API.
        Returns:
            List[schemas.HourlyRawInCimisReponse]: List of HourlyRawData objects
                containing hourly raw data from the target stations

        Raises:
            ValueError: If the response body does not contain valid JSON.
            KeyError: If the JSON dictionary does not contain the expected properties.
            requests.ConnectionError: If a Connection error occurred.
            requests.HTTPError: If an HTTP error occurred.
            requests.Timeout: If the request timed out.        
        """
        pass


class DailyRawDataService():

    __base_url = config.CIMIS_API_DATA_BASE_URL

    __data_items = [
        "day-air-tmp-avg",
        "day-air-tmp-max",
        "day-air-tmp-min",
        "day-dew-pnt",
        "day-eto",
        "day-asce-eto",
        "day-asce-etr",
        "day-precip",
        "day-rel-hum-avg",
        "day-rel-hum-max",
        "day-rel-hum-min",
        "day-soil-tmp-avg",
        "day-soil-tmp-max",
        "day-soil-tmp-min",
        "day-sol-rad-avg",
        "day-sol-rad-net",
        "day-vap-pres-max",
        "day-vap-pres-avg",
        "day-wind-ene",
        "day-wind-ese",
        "day-wind-nne",
        "day-wind-nnw",
        "day-wind-run",
        "day-wind-spd-avg",
        "day-wind-ssw",
        "day-wind-wnw",
        "day-wind-wsw"
    ]
    
    # -------------------------------------------------------------------------
    # Private helper methods
    # -------------------------------------------------------------------------



    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------

