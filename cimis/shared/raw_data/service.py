import os
import logging
from typing import List
from datetime import date


from sqlalchemy.sql.sqltypes import Date
import pydantic
import requests
from requests.models import Response


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
    def __parse_cimis_response(response: requests.Response) -> List[schemas.HourlyRawInCimisResponse]:
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
        json = response.json()
        records = json['Data']['Providers'][0]['Records']
        return pydantic.parse_obj_as(List[schemas.HourlyRawInCimisResponse], records)

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------
    @classmethod
    def to_hourlyraw_schema(cls, station_data: List[schemas.HourlyRawInCimisResponse]) -> List[schemas.HourlyRaw]:
        """Converts hourlyraw schema from HourlyRawInCimisResponse to HourlyRaw"""
        return [
            schemas.HourlyRaw(
                StationId=data.Station,
                Date=utils.parse_cimis_date_str(data.Date),
                Hour=utils.parse_cimis_hour_str(data.Hour),
                HlyAirTmp=data.HlyAirTmp['Value'],
                HlyAirTmpQc=data.HlyAirTmp['Qc'],
                HlyAirTmpUnits=data.HlyAirTmp['Unit'],
                HlyDewPnt=data.HlyDewPnt['Value'],
                HlyDewPntQc=data.HlyDewPnt['Qc'],
                HlyDewPntUnits=data.HlyDewPnt['Unit'],
                HlyEto=data.HlyEto['Value'],
                HlyEtoQc=data.HlyEto['Qc'],
                HlyEtoUnits=data.HlyEto['Unit'],
                HlyNetRad=data.HlyNetRad['Value'],
                HlyNetRadQc=data.HlyNetRad['Qc'],
                HlyNetRadUnits=data.HlyNetRad['Unit'],
                HlyAsceEto=data.HlyAsceEto['Value'],
                HlyAsceEtoQc=data.HlyAsceEto['Qc'],
                HlyAsceEtoUnits=data.HlyAsceEto['Unit'],
                HlyAsceEtr=data.HlyAsceEtr['Value'],
                HlyAsceEtrQc=data.HlyAsceEtr['Qc'],
                HlyAsceEtrUnits=data.HlyAsceEtr['Unit'],
                HlyPrecip=data.HlyPrecip['Value'],
                HlyPrecipQc=data.HlyPrecip['Qc'],
                HlyPrecipUnits=data.HlyPrecip['Unit'],
                HlyRelHum=data.HlyRelHum['Value'],
                HlyRelHumQc=data.HlyRelHum['Qc'],
                HlyRelHumUnits=data.HlyRelHum['Unit'],
                HlyResWind=data.HlyResWind['Value'],
                HlyResWindQc=data.HlyResWind['Qc'],
                HlyResWindUnits=data.HlyResWind['Unit'],
                HlySoilTmp=data.HlySoilTmp['Value'],
                HlySoilTmpQc=data.HlySoilTmp['Qc'],
                HlySoilTmpUnits=data.HlySoilTmp['Unit'],
                HlySolRad=data.HlySolRad['Value'],
                HlySolRadQc=data.HlySolRad['Qc'],
                HlySolRadUnits=data.HlySolRad['Unit'],
                HlyVapPres=data.HlyVapPres['Value'],
                HlyVapPresQc=data.HlyVapPres['Qc'],
                HlyVapPresUnits=data.HlyVapPres['Unit'],
                HlyWindDir=data.HlyWindDir['Value'],
                HlyWindDirQc=data.HlyWindDir['Qc'],
                HlyWindDirUnits=data.HlyWindDir['Unit'],
                HlyWindSpd=data.HlyWindSpd['Value'],
                HlyWindSpdQc=data.HlyWindSpd['Qc'],
                HlyWindSpdUnits=data.HlyWindSpd['Unit'],
            )
            for data in station_data
        ]

    @classmethod
    def get_hourlyraw_data_from_cimis(cls, start_date: date, end_date: date, targets: List[int] = None) -> List[schemas.HourlyRawInCimisResponse]:
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
            ValueError: If the response body does not contain valid JSON, or targets list is empty
            KeyError: If the JSON dictionary does not contain the expected properties.
            requests.ConnectionError: If a Connection error occurred.
            requests.HTTPError: If an HTTP error occurred.
            requests.Timeout: If the request timed out.        
        """
        # Throw ValueError if targets is empty
        if len(targets) == 0:
            raise ValueError('List[targets] cannot be empty.')

        # Build CIMIS request URL
        cimis_request_url = utils.build_cimis_request_url(base_url=cls.__base_url, 
                                                            targets=targets,
                                                            data_items=cls.__data_items,
                                                            start_date=start_date,
                                                            end_date=end_date)

        print(cimis_request_url)

        # Request CIMIS API data with appropriate headers
        headers = {'accept':'application/json'}
        response = requests.get(cimis_request_url, headers=headers, timeout=config.HTTP_TIMEOUT_SECONDS)
        response.raise_for_status()
        hourly_raw_data = cls.__parse_cimis_response(response)
        return [data for data in hourly_raw_data]

        

        


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

