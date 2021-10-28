from typing import List, Tuple
from datetime import date
import logging

import pydantic
import requests

from shared.message import actions
from shared.core import config, db, utils
from shared.main_data import schemas, models

class MainDataService:

    def __init__(self, action):
        self.__action = action

    __base_url = config.CIMIS_API_DATA_BASE_URL

    __hourly_data_items = [
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

    __daily_data_items = [
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
    def __get_sister_station(self, station_id: int) -> Tuple[int, int]:
        """Retrieves raw data from CIMIS API.

        Args:
            station_id: Id of station to get sister stations for
        
        Returns:
            sister_stations: Sister stations of station_id

        Raises:
            requests.ConnectionError: If a Connection error occurred.
            requests.HTTPError: If an HTTP error occurred.
            requests.Timeout: If the request timed out.        
        """
        data_as_list = []
        table = config.SQL_SISTERSTATION_TABLE
        schema = schemas.Sister

        with db.engine.connect() as connection:
            # SQL Query
            data = connection.execute(f"SELECT StationId, FirstSisterId, SecondSisterId\
                                        FROM {table}\
                                        WHERE StationId = {station_id}")
            for item in data:
                data_as_list.append(dict(item))

        sister_stations = pydantic.parse_obj_as(List[schema], data_as_list)
        return (sister_stations[0].FirstSisterId, sister_stations[0].SecondSisterId)

    def get_historical_data(self, targets: List[int], start_date: date, end_date: date) -> List:
        """Retrieves historical data from the database"""
        pass

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------

    def get_data_from_db(self):
        pass

    def clean_data_from_db(self):
        pass

