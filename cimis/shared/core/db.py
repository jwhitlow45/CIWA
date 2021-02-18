import urllib
import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from shared.core import config

engine = create_engine(config.SQLALCHEMY_URL)
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
