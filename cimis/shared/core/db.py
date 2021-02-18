import urllib
import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from shared.core import config

# connection string
pyodbc_conn_str = (
    f'DRIVER={config.SQL_SERVER_DRIVER}'
    f'SERVER={config.SQL_SERVER_NAME}'
    f'PORT={config.SQL_SERVER_PORT}'
    f'DATABSE={config.SQL_DATABASE_NAME}'
    f'UID={config.SQL_SERVER_USERNAME}'
    f'PWD={config.SQL_SERVER_PASSWORD}'
)

params = urllib.parse.quote_plus(pyodbc_conn_str)

# SQLAlchemy
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
Base = declarative_base()
Session = sessionmaker(bind=engine)

@contextlib.contextmanager
def session_manager():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
