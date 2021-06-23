import os
from typing import List
import datetime

def get_utc_timestamp():
    return datetime.datetime.utcnow()\
            .replace(tzinfo=datetime.timezone.utc)\
            .isoformat()

def parse_date_str(date_str: str) -> datetime.date:
    """Parses the date string of format YYYY-MM-DD or YYYY/MM/DD

    Args:
        date_str: Date string in the format mm/dd/yyyy.

    Returns:
        datetime.date: Datetime object date of same date
    """
    if '/' in date_str:
        [month, day, year] = date_str.split('/')
        return datetime.date(int(year), int(month), int(day))
    if '-' in date_str:
        [year, month, day] = date_str.split('-')
        return datetime.date(int(year), int(month), int(day))

def parse_hour_str(hour_str: str) -> datetime.time:
    """Parses the hour string format of HHMM

    Args:
        hour_str: Hour string in format hhmm.

    Returns:
        datetime.hour: Datetime object hour of same hour
    """
    hr = hour_str[0:2]  # Strip first chars to get hour
    hr = int(hr) - 1    # Convert hour to range 0-23 from 1-24
    return datetime.time(hour=hr, minute=0) # Minute is always 0

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

    # App key for accessing CIMIS API
    appKey = ('?appKey=' + os.getenv("CIMIS_API_KEY"))
    # Target stations
    str_targets = f'&targets={str(targets)[1:-1].replace(" ", "")}'
    # Data items
    str_data_items = f'&dataItems={str(data_items)[1:-1].replace(" ", "")}'
    str_data_items = str_data_items.replace("'", "") # Remove '' from strings 
    # Start date
    str_start_date = f'&startDate={start_date.strftime("%Y-%m-%d")}'
    # End date
    str_end_date= f'&endDate={end_date.strftime("%Y-%m-%d")}' 
    # Build URL
    url = f'{base_url + appKey + str_targets + str_data_items + str_start_date + str_end_date}'

    return url

def int_to_binary_string(num: int, num_bits: int) -> str:
    """Convert integer to binary string of size number of bits
    
    Args:
        num: Integer to be converted to binary string

    Returns:
        str: Binary string representation of an integer

    Raises:
        OverflowError: If num_bits is too small to contain num
    """
    binary_string = str(bin(num))[2:].zfill(num_bits)
    if len(binary_string) > num_bits:
        raise OverflowError
    return binary_string

def generate_raw_data_primary_key(station_num: int, date: datetime.date, hour: datetime.time = datetime.time(0, 0)) -> int:
    """Creates unique key for raw data items in raw data table based on
    station number, date, and Optional[hour] of the data
    
        station_num: station number, range(2^10)
        date.year: years since 1970, range(2^8)
        date.month: month of year, range(2^4)
        date.day: date of the month, range(2^5)
        hour.hour: hour of the day, range(2^5)
    """
    station_key = int_to_binary_string(station_num, 10)
    date_key = (int_to_binary_string(date.year - 1970, 8) +
                int_to_binary_string(date.month, 4) +
                int_to_binary_string(date.day, 5))
    hour_key = int_to_binary_string(hour.hour, 5)
    return int(station_key + date_key + hour_key, 2)

def is_below_cimis_hourly_record_limit(targets: List[int], start_date: datetime.date, end_date:datetime.date) -> bool:
    """Check if hourly request is exceeding record limit set by CIMIS"""
    days_requested = (end_date - start_date).days + 1
    # Return the result of (days requested * hours per day * number of stations) <= 1750
    return (days_requested*24*len(targets)) <= 1750

def is_below_cimis_daily_record_limit(targets: List[int], start_date: datetime.date, end_date:datetime.date):
    """Check if daily request is exceeding record limit set by CIMIS"""
    days_requested = (end_date - start_date).days + 1
    # Return the result of (days requested * number of stations) <= 1750
    return (days_requested*len(targets)) <= 1750