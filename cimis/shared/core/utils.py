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