import os

from dotenv import find_dotenv, load_dotenv

# Load env vars from .env file.
load_dotenv(find_dotenv())

# HTTP Requests
HTTP_TIMEOUT_SECONDS = 30
