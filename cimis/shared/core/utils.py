import os
from typing import List
import datetime

def get_utc_timestamp():
    return datetime.datetime.utcnow()\
            .replace(tzinfo=datetime.timezone.utc)\
            .isoformat()

def parse_cimis_date_str(date_str: str) -> datetime.date:
    """Parses the date string format used by CIMIS.

    Args:
        date_str: Date string in the format mm/dd/yyyy.

    Returns:
        datetime.date: The date obje as sa
    """
    [month, day, year] = date_str.split('/')
    return datetime.date(int(year), int(month), int(day))

def parse_cimis_coordinate_str(coord_str: str) -> float:
    """Parses the coordinate string format used by CIMIS.

    Args:
        coord_str: Coordinate string in the format 'HMS / DD'.

    Returns:
        float: The coordinate in decimal degrees.
    """
    [hms, dd] = coord_str.split('/')
    return float(dd)

def build_cimis_request_url(base_url: str, targets: List[int], data_items: List[str], start_date: datetime.date, end_date: datetime.date) -> str:
    """Builds CIMIS RestAPI request URL
    
    Args:
        base_url: String containing base url for request
        List[targets]: Integer list of stations to gather data from
        List[data_items]: Data items to gather from CIMIS API
        start_date: Date to start gathering data from
        end_date: Date to stop gather data at

    Returns:
        str: String containing CIMIS API request URL
    """

    # Establish url to append to
    url = base_url
    # Add app key for accessing CIMIS API
    url += ('?appKey=' + os.getenv("CIMIS_API_KEY"))
    # Add targets to URL request
    url += '&targets='
    for target in targets:
        url += (str(target) + ',')
    url = url[:-1] # Remove trailing comma
    # Add all data items to URL request
    url += '&dataItems='
    for item in data_items:
        url += (item + ',')
    url = url[:-1] # Remove trailing comma
    # Add start date
    url += '&startDate='
    url += start_date.strftime("%Y-%m-%d")
    # Add end date
    url += '&endDate='
    url += end_date.strftime("%Y-%m-%d") 

    return url