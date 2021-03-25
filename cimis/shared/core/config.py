import os

from dotenv import find_dotenv, load_dotenv

# Load env vars from .env file.
load_dotenv(find_dotenv())

# HTTP Requests
HTTP_TIMEOUT_SECONDS = 30

# CIMIS
CIMIS_API_KEY = os.getenv("CIMIS_API_KEY")
CIMIS_API_DATA_BASE_URL = "http://et.water.ca.gov/api/data"
CIMIS_API_STATION_BASE_URL = "http://et.water.ca.gov/api/station"

# SQL Server
SQL_SERVER_NAME = os.getenv("SQL_SERVER_NAME")
SQL_SERVER_PORT = os.getenv("SQL_SERVER_PORT")
SQL_DATABASE_NAME = os.getenv("SQL_DATABASE_NAME")
SQL_SERVER_USERNAME = os.getenv("SQL_SERVER_USERNAME")
SQL_SERVER_PASSWORD = os.getenv("SQL_SERVER_PASSWORD")
SQL_SERVER_DRIVER = os.getenv("SQL_SERVER_DRIVER")

SQLALCHEMY_URL = (
    f'mssql+pyodbc://{SQL_SERVER_USERNAME}:{SQL_SERVER_PASSWORD}'
    f'@{SQL_SERVER_NAME}:{SQL_SERVER_PORT}/{SQL_DATABASE_NAME}?'
    f'driver={"+".join(SQL_SERVER_DRIVER.strip("{").strip("}").split(" "))}'
)

# Service Bus
SERVICE_BUS_CONNECTION_STRING = os.getenv('SERVICE_BUS_CONNECTION_STRING')
SERVICE_BUS_STATION_QUEUE_NAME = os.getenv('SERVICE_BUS_STATION_QUEUE_NAME')
SERVICE_BUS_RAW_QUEUE_NAME = os.getenv('SERVICE_BUS_RAW_QUEUE_NAME')
SERVICE_BUS_MAIN_QUEUE_NAME = os.getenv('SERVICE_BUS_MAIN_QUEUE_NAME')

# Max times message will be put back on queue
MAX_DELIVERY_COUNT = 32
