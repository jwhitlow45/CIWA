from typing import List
from datetime import date
import logging

import pydantic
import requests

from shared.message import actions
from shared.core import config, db, utils
from shared.raw_data import schemas, models


class RawDataService:

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

    @staticmethod
    def __parse_cimis_response(action, response: requests.Response) -> List:
        """
            Args:
                action: action to determine which action type is being parsed
                response: The JSON response provided by the CIMIS API
            Returns:
                List[schemas.*RawInCimisResponse]: List of record objects for
                each station in the JSON response
            Raises:
                ValueError: If the response body does not contain valid JSON.
                KeyError: If the JSON dictionaryy does not contain expected properties
        """
        json = response.json()
        records = json['Data']['Providers'][0]['Records']
        objects: any
        if action.action_type == actions.ActionType.DATA_ADD_DAILY_RAW:
            objects = pydantic.parse_obj_as(
                List[schemas.DailyRawInCimisResponse], records)
        elif action.action_type == actions.ActionType.DATA_ADD_HOURLY_RAW:
            objects = pydantic.parse_obj_as(
                List[schemas.HourlyRawInCimisResponse], records)
        else:
            raise TypeError('Invalid action type.')
        return objects

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------
    def to_raw_schema(self, station_data: List) -> List:
        """Converts raw schema from *RawInCimisResponse to *Raw"""
        if self.__action.action_type == actions.ActionType.DATA_ADD_DAILY_RAW:
            return [
                schemas.DailyRaw(
                    Id=utils.generate_data_primary_key(data.Station,
                                                       utils.parse_date_str(data.Date)),
                    StationId=data.Station,
                    Date=utils.parse_date_str(data.Date),
                    DayAirTmpAvg=data.DayAirTmpAvg['Value'],
                    DayAirTmpAvgQc=data.DayAirTmpAvg['Qc'],
                    DayAirTmpAvgUnits=data.DayAirTmpAvg['Unit'],
                    DayAirTmpMax=data.DayAirTmpMax['Value'],
                    DayAirTmpMaxQc=data.DayAirTmpMax['Qc'],
                    DayAirTmpMaxUnits=data.DayAirTmpMax['Unit'],
                    DayAirTmpMin=data.DayAirTmpMin['Value'],
                    DayAirTmpMinQc=data.DayAirTmpMin['Qc'],
                    DayAirTmpMinUnits=data.DayAirTmpMin['Unit'],
                    DayDewPnt=data.DayDewPnt['Value'],
                    DayDewPntQc=data.DayDewPnt['Qc'],
                    DayDewPntUnits=data.DayDewPnt['Unit'],
                    DayEto=data.DayEto['Value'],
                    DayEtoQc=data.DayEto['Qc'],
                    DayEtoUnits=data.DayEto['Unit'],
                    DayAsceEto=data.DayAsceEto['Value'],
                    DayAsceEtoQc=data.DayAsceEto['Qc'],
                    DayAsceEtoUnits=data.DayAsceEto['Unit'],
                    DayAsceEtr=data.DayAsceEtr['Value'],
                    DayAsceEtrQc=data.DayAsceEtr['Qc'],
                    DayAsceEtrUnits=data.DayAsceEtr['Unit'],
                    DayPrecip=data.DayPrecip['Value'],
                    DayPrecipQc=data.DayPrecip['Qc'],
                    DayPrecipUnits=data.DayPrecip['Unit'],
                    DayRelHumAvg=data.DayRelHumAvg['Value'],
                    DayRelHumAvgQc=data.DayRelHumAvg['Qc'],
                    DayRelHumAvgUnits=data.DayRelHumAvg['Unit'],
                    DayRelHumMax=data.DayRelHumMax['Value'],
                    DayRelHumMaxQc=data.DayRelHumMax['Qc'],
                    DayRelHumMaxUnits=data.DayRelHumMax['Unit'],
                    DayRelHumMin=data.DayRelHumMin['Value'],
                    DayRelHumMinQc=data.DayRelHumMin['Qc'],
                    DayRelHumMinUnits=data.DayRelHumMin['Unit'],
                    DaySoilTmpAvg=data.DaySoilTmpAvg['Value'],
                    DaySoilTmpAvgQc=data.DaySoilTmpAvg['Qc'],
                    DaySoilTmpAvgUnits=data.DaySoilTmpAvg['Unit'],
                    DaySoilTmpMax=data.DaySoilTmpMax['Value'],
                    DaySoilTmpMaxQc=data.DaySoilTmpMax['Qc'],
                    DaySoilTmpMaxUnits=data.DaySoilTmpMax['Unit'],
                    DaySoilTmpMin=data.DaySoilTmpMin['Value'],
                    DaySoilTmpMinQc=data.DaySoilTmpMin['Qc'],
                    DaySoilTmpMinUnits=data.DaySoilTmpMin['Unit'],
                    DaySolRadAvg=data.DaySolRadAvg['Value'],
                    DaySolRadAvgQc=data.DaySolRadAvg['Qc'],
                    DaySolRadAvgUnits=data.DaySolRadAvg['Unit'],
                    DaySolRadNet=data.DaySolRadNet['Value'],
                    DaySolRadNetQc=data.DaySolRadNet['Qc'],
                    DaySolRadNetUnits=data.DaySolRadNet['Unit'],
                    DayVapPresAvg=data.DayVapPresAvg['Value'],
                    DayVapPresAvgQc=data.DayVapPresAvg['Qc'],
                    DayVapPresAvgUnits=data.DayVapPresAvg['Unit'],
                    DayVapPresMax=data.DayVapPresMax['Value'],
                    DayVapPresMaxQc=data.DayVapPresMax['Qc'],
                    DayVapPresMaxUnits=data.DayVapPresMax['Unit'],
                    DayWindEne=data.DayWindEne['Value'],
                    DayWindEneQc=data.DayWindEne['Qc'],
                    DayWindEneUnits=data.DayWindEne['Unit'],
                    DayWindEse=data.DayWindEse['Value'],
                    DayWindEseQc=data.DayWindEse['Qc'],
                    DayWindEseUnits=data.DayWindEse['Unit'],
                    DayWindNne=data.DayWindNne['Value'],
                    DayWindNneQc=data.DayWindNne['Qc'],
                    DayWindNneUnits=data.DayWindNne['Unit'],
                    DayWindNnw=data.DayWindNnw['Value'],
                    DayWindNnwQc=data.DayWindNnw['Qc'],
                    DayWindNnwUnits=data.DayWindNnw['Unit'],
                    DayWindRun=data.DayWindRun['Value'],
                    DayWindRunQc=data.DayWindRun['Qc'],
                    DayWindRunUnits=data.DayWindRun['Unit'],
                    DayWindSsw=data.DayWindSsw['Value'],
                    DayWindSswQc=data.DayWindSsw['Qc'],
                    DayWindSswUnits=data.DayWindSsw['Unit'],
                    DayWindWnw=data.DayWindWnw['Value'],
                    DayWindWnwQc=data.DayWindWnw['Qc'],
                    DayWindWnwUnits=data.DayWindWnw['Unit'],
                    DayWindWsw=data.DayWindWsw['Value'],
                    DayWindWswQc=data.DayWindWsw['Qc'],
                    DayWindWswUnits=data.DayWindWsw['Unit']
                )
                for data in station_data
            ]
        elif self.__action.action_type == actions.ActionType.DATA_ADD_HOURLY_RAW:
            return [
                schemas.HourlyRaw(
                    Id=utils.generate_data_primary_key(data.Station,
                                                       utils.parse_date_str(
                                                           data.Date),
                                                       utils.parse_hour_str(data.Hour)),
                    StationId=data.Station,
                    Date=utils.parse_date_str(data.Date),
                    Hour=utils.parse_hour_str(data.Hour),
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
        else:
            raise TypeError('Invalid action type.')

    def get_raw_data_from_cimis(self, start_date: date, end_date: date, targets: List[int] = None):
        """Retrieves raw data from CIMIS API.

        Args:
            startDate: Date from which data will start to be gathered
            endDate: Date to which data will stop being gathered
            targets: If not None, returns raw data for only the target station ids.
        Returns:
            schemas.*: *RawData objects containing raw data from the target stations

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
        # Headers for CIMIS request
        headers = {'accept': 'application/json'}
        # Build request URL
        if self.__action.action_type == actions.ActionType.DATA_ADD_DAILY_RAW:
            data_items = self.__daily_data_items
        elif self.__action.action_type == actions.ActionType.DATA_ADD_HOURLY_RAW:
            data_items = self.__hourly_data_items
        else:
            raise KeyError('Invalid action type.')
        cimis_request_url = utils.build_cimis_request_url(base_url=self.__base_url,
                                                          targets=targets,
                                                          data_items=data_items,
                                                          start_date=start_date,
                                                          end_date=end_date)
        # Request CIMIS API data with appropriate headers
        response = requests.get(
            cimis_request_url, headers=headers, timeout=config.HTTP_TIMEOUT_SECONDS)
        response.raise_for_status()
        # Parse raw data
        raw_data = self.__parse_cimis_response(self.__action, response)
        # Return raw data
        return raw_data

    def get_data_from_db(self, targets: List[int], start_date: date, end_date: date) -> dict:
        """Retrieves raw data from the database"""
        # Determine type to parse as
        data_dict = {}
        table: str
        if self.__action.action_type == actions.ActionType.DATA_ADD_DAILY_RAW:
            table = config.SQL_DAILYRAW_TABLE
        elif self.__action.action_type == actions.ActionType.DATA_ADD_HOURLY_RAW:
            table = config.SQL_HOURLYRAW_TABLE
        else:
            raise TypeError('Invalid action type.')

        # Connect to database and retrieve data
        with db.engine.connect() as connection:
            # SQL Query
            data = connection.execute(f"SELECT Id, StationId, Date, *\
                                        FROM {table}\
                                        WHERE StationId IN ({str(targets)[1:-1]})\
                                        AND Date BETWEEN '{start_date.strftime('%Y-%m-%d')}'\
                                        AND '{end_date.strftime('%Y-%m-%d')}'")
            for item in data:
                data_dict[dict(item)['Id']] = dict(item)
        return data_dict

    def insert_raw_data(self, data_list: List):
        """Adds raw data to database"""
        if self.__action.action_type == actions.ActionType.DATA_ADD_DAILY_RAW:
            table = config.SQL_DAILYRAW_TABLE
            model = models.DailyRawData
        elif self.__action.action_type == actions.ActionType.DATA_ADD_HOURLY_RAW:
            table = config.SQL_HOURLYRAW_TABLE
            model = models.HourlyRawData

        with db.session_manager() as session:
            logging.info(f'Staging changes for {table}')
            session.add_all([model(**data.dict()) for data in data_list])
            logging.info(
                f'Committing changes to {table}. Estimated time: {len(data_list)/config.SQL_AVG_INSERTS_PER_SECOND:.1f} seconds.')
            session.commit()
            logging.info(
                f'All changes have been successfully commited to {table}.')
