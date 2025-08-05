

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# path to database file
DATABASE_URL = "sqlite:///habits.db"

# create engine and connection to the database
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Session-Factory: new connection for each session
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """
    create the database tables, if they don't exist yet.
    """
    Base.metadata.create_all(bind=engine)

def get_session():
    """
    create and return a new database session.
    Usage example:
        with get_session() as session:
            ...
    """
    return SessionLocal()