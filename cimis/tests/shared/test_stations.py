import json
from typing import List
from unittest import TestCase
from unittest.mock import patch

import pydantic

from shared.stations import schemas
from shared.stations import service
from shared.stations.service import StationService

mock_station_response = {
    "Stations": [
        {
            "StationNbr": "1",
            "Name": "Fresno/F.S.U. USDA",
            "City": "Fresno",
            "RegionalOffice": "South Central Region Office",
            "County": "Fresno",
            "ConnectDate": "6/7/1982",
            "DisconnectDate": "9/25/1988",
            "IsActive": "False",
            "IsEtoStation": "True",
            "Elevation": "340",
            "GroundCover": "Grass",
            "HmsLatitude": "36º48'52N / 36.814444",
            "HmsLongitude": "-119º43'54W / -119.731670",
            "ZipCodes": [
                "93766",
            ],
            "SitingDesc": ""
        },
        {
            "StationNbr": "2",
            "Name": "FivePoints",
            "City": "Five Points",
            "RegionalOffice": "South Central Region Office",
            "County": "Fresno",
            "ConnectDate": "6/7/1982",
            "DisconnectDate": "12/31/2050",
            "IsActive": "True",
            "IsEtoStation": "True",
            "Elevation": "285",
            "GroundCover": "Grass",
            "HmsLatitude": "36º20'10N / 36.336222",
            "HmsLongitude": "-120º6'46W / -120.112910",
            "ZipCodes": [
                "93624"
            ],
            "SitingDesc": ""
        }
    ]
}


def mocked_requests_get(*args, **kwargs):

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(mock_station_response, 200)


def mocked_request_get_with_error(*args, **kwargs):

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(mock_station_response, 400)


class TestStationService(TestCase):

    @classmethod
    def setUp(cls):
        cls.all_stations = pydantic.parse_obj_as(
            List[schemas.StationInCimisResponse],
            mock_station_response['Stations']
        )

    @patch('shared.stations.service.requests.get')
    def test_get_stations_from_cimis_without_targets(self, mocked_requests_get):
        stations = StationService.get_stations_from_cimis()
        self.assertListEqual(stations, self.all_stations)

    @patch('shared.stations.service.requests.get', mocked_requests_get)
    def test_get_stations_from_cimis_with_targets(self):
        targets = [2]
        stations = StationService.get_stations_from_cimis(targets=targets)
        expected = [station for station in self.all_stations if station.StationNbr in targets]
        self.assertListEqual(stations, expected)

    @patch('shared.stations.service.requests.get', mocked_request_get_with_error)
    def test_get_stations_from_cimis_with_http_error(self):
        with self.assertRaises(Exception):
            StationService.get_stations_from_cimis()
