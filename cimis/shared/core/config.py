import os

from dotenv import find_dotenv, load_dotenv

# Load env vars from .env file.
load_dotenv(find_dotenv())

# HTTP Requests
HTTP_TIMEOUT_SECONDS = 30

# SQL SERVER
SQL_SERVER_NAME = os.getenv("SQL_SERVER_NAME")
SQL_SERVER_PORT = os.getenv("SQL_SERVER_PORT")
SQL_DATABASE_NAME = os.getenv("SQL_DATABASE_NAME")
SQL_SERVER_USERNAME = os.getenv("SQL_SERVER_USERNAME")
SQL_SERVER_PASSWORD = os.getenv("SQL_SERVER_PASSWORD")
SQL_SERVER_DRIVER = os.getenv("SQL_SERVER_DRIVER")

# Alembic
ALEMBIC_SQLALCHEMY_URL = (
    f'mssql+pyodbc://{SQL_SERVER_USERNAME}:{SQL_SERVER_PASSWORD}'
    f'@{SQL_SERVER_NAME}:{SQL_SERVER_PORT}/{SQL_DATABASE_NAME}?'
    f'driver={"+".join(SQL_SERVER_DRIVER.strip("{").strip("}").split(" "))}'
)