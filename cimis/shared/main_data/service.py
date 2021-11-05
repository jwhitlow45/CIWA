from typing import List, Tuple
from datetime import date, time
import logging

import pydantic
import requests
import copy

from shared.message import actions
from shared.core import config, db, utils
from shared.main_data import schemas, models
from shared.raw_data.service import RawDataService


class MainDataService:

    def __init__(self, action):
        self.__action = action

    __hourly_hist_data_items = [
        "HlyAirTmp",
        "HlyDewPnt",
        "HlyEto",
        "HlyAsceEto",
        "HlyPrecip",
        "HlyRelHum",
        "HlySoilTmp",
        "HlySolRad",
        "HlyWindDir",
        "HlyWindSpd"
    ]

    __daily_hist_data_map = {
        "DayAirTmpMax": "Tmax",
        "DayAirTmpMin": "Tmin",
        "DayEto": "Eto",
        "DayAsceEto": "AsceETo",
        "DayPrecip": "Precip",
        "DayRelHumMax": "Rhmax",
        "DayRelHumMin": "Rhmin",
        "DayWindSpdAvg": "Wind"
    }

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
                                        AND Date >= '2000-{start_date.strftime('%m-%d')}'\
                                        AND Date <= '2000-{end_date.strftime('%m-%d')}'")
            for item in data:
                data_primary_key: int
                item = dict(item)
                if self.__action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
                    data_primary_key = utils.generate_data_primary_key(
                        item['StationId'], item['Date'])
                elif self.__action.action_type == actions.ActionType.DATA_CLEAN_HOURLY_RAW:
                    data_primary_key = utils.generate_data_primary_key(
                        item['StationId'], date=item['Date'], hour=item['Hour'])
                else:
                    raise TypeError('Invalid action type.')
                data_dict[data_primary_key] = item

        return data_dict

    def clean_data_from_db(self, raw_data: dict,
                           historical_data: dict,
                           RDS: RawDataService) -> dict:
        """Cleans raw data and stores in main data tables"""
        flags_to_clean = ['N', 'M', 'Q']

        HIST_FLAG = 'RH'
        SIST_FLAG = 'RS'

        data_members: any
        if self.__action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
            data_members = self.__daily_hist_data_map
        elif self.__action.action_type == actions.ActionType.DATA_CLEAN_HOURLY_RAW:
            data_members = self.__hourly_hist_data_items

        for row in raw_data.values():
            for data_member in data_members:
                data_member_qc = str(data_member + 'Qc')
                if row[data_member_qc] in flags_to_clean:
                    hist_data_member: dict
                    if self.__action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
                        hist_data_member = self.__daily_hist_data_map[data_member]

                    # Get sister station data
                    sister_stations = self.__get_sister_station(
                        row['StationId'])
                    sister_data_one = RDS.get_data_from_db([sister_stations[0]],
                                                           row['Date'],
                                                           row['Date'])
                    sister_data_two = RDS.get_data_from_db([sister_stations[1]],
                                                           row['Date'],
                                                           row['Date'])

                    if sister_data_one != {} and sister_data_one[data_member_qc] not in flags_to_clean:
                        row[data_member] = sister_data_one[data_member]
                        row[data_member_qc] = SIST_FLAG
                    elif sister_data_two != {} and sister_data_two[data_member_qc] not in flags_to_clean:
                        row[data_member] = sister_data_two[data_member]
                        row[data_member_qc] = SIST_FLAG
                    else:
                        if self.__action.action_type == actions.ActionType.DATA_CLEAN_DAILY_RAW:
                            hist_date = date(year=2000,
                                             month=row['Date'].month,
                                             day=row['Date'].day)
                            hist_id = utils.generate_data_primary_key(row['StationId'],
                                                                      hist_date)
                            row[data_member] = historical_data[hist_id][hist_data_member]
                            row[data_member_qc] = HIST_FLAG
                        elif self.__action.action_type == actions.ActionType.DATA_CLEAN_HOURLY_RAW:
                            hist_date = date(year=2000,
                                             month=row['Date'].month,
                                             day=row['Date'].day)
                            hist_hour = time(hour=row['Hour'].hour,
                                             minute=row['Hour'].minute)
                            hist_id = utils.generate_data_primary_key(row['StationId'],
                                                                      hist_date,
                                                                      hist_hour)
                            row[data_member] = historical_data[hist_id][data_member]
                            row[data_member_qc] = HIST_FLAG
            
        return raw_data