import logging
from typing import List
import pprint

import azure.functions as func
from datetime import date

from shared.raw_data.service import HourlyRawDataService
from shared.core import utils
from shared.core import config


def testing():
    startDate = date(2010,1,1)
    endDate = date(2010,1,2)
    stations = [2,8]

    myData = HourlyRawDataService.get_hourlyraw_data_from_cimis(targets=stations,
                                                                start_date=startDate,
                                                                end_date=endDate)
    myObjects = HourlyRawDataService.to_hourlyraw_schema(myData)
    for item in myObjects:
        pprint(item)
    logging.info("Completed import")              

    
    

def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
    testing()
