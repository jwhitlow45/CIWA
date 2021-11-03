from typing import List, Tuple
from datetime import date
import logging

import pydantic
import requests

from shared.message import actions
from shared.core import config, db, utils
from shared.main_data import schemas, models
from shared.raw_data.service import RawDataService

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
        """Retrieves sister stations from sister station table.

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

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------

    def get_historical_data(self, targets: List[int], start_date: date, end_date: date) -> dict:
        """Retrieves historical data from the database"""
        data_dict = {}
        table: any

        # Select proper SQL table and schema
        if self.__action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
            table = config.SQL_DAILYHISTORY_TABLE
        elif self.__action.action_type == actions.ActionType.DATA_CLEAN_HOURLY_RAW:
            table = config.SQL_HOURLYHISTORY_TABLE
        else:
            raise TypeError('Invalid action type.')

        with db.engine.connect() as connection:
            # SQL Query
            data = connection.execute(f"SELECT *\
                                        FROM {table}\
                                        WHERE StationId IN ({str(targets)[1:-1]})\
                                        AND Date BETWEEN '2000-{start_date.strftime('%m-%d')}'\
                                        AND '2000-{end_date.strftime('%m-%d')}'")
            for item in data:
                data_dict[dict(item)['Id']] = dict(item)
        return data_dict

   
    def clean_data_from_db(self, raw_data, historical_data) -> None:
        """Cleans raw data and stores in main data tables"""

        pass

