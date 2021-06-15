import pydantic
import requests

from shared.core import config
from shared.core import db
from shared.core import utils

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
    