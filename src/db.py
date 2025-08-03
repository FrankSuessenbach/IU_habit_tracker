

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Datenbankpfad (SQLite-Datei im Projektverzeichnis)
DATABASE_URL = "sqlite:///habits.db"

# Engine erstellen (Verbindung zur DB)
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Session-Factory: Jede Sitzung ist eine neue DB-Verbindung
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """
    Erstellt alle Tabellen, falls sie noch nicht existieren.
    """
    Base.metadata.create_all(bind=engine)

def get_session():
    """
    Erzeugt und gibt eine neue Datenbank-Session zurück.
    Nutzung z.B. via:  
        with get_session() as session:
            ...
    """
    return SessionLocal()