from typing import List, Tuple
from datetime import date
import logging

import pydantic
import requests

from shared.message import actions
from shared.core import config, db, utils
from shared.raw_data import schemas, models

class MainDataService:

    def __init__(self, action):
        self.__action == action

    __base_url = config.CIMIS_APIT_DATA_BASE_URL

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
        pass

    def __get_historical_data(self, targets: List[int], start_date: date, end_date: date) -> List:
        pass

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------

    def get_data_from_db(self):
        pass

    def clean_data_from_db(self):
        pass

