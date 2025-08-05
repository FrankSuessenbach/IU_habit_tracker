
from .db import init_db, get_session
from .manager import HabitManager
from .interface import interface

def main():
    init_db()  # Initialize the database

    with get_session() as session:
        manager = HabitManager(session)
        cli = interface(manager)
        cli.main_menu()

if __name__ == "__main__":
    main()
    