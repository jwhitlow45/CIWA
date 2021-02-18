from typing import List

import requests

from shared.stations import schemas


class StationService:

    @classmethod
    def get_stations_from_cimis(cls, targets: List[int] = None) -> List[schemas.Station]:
        pass
