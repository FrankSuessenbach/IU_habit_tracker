
from datetime import datetime
from sqlalchemy.orm import Session
from .models import Habit


class HabitManager:
    """
    Manages operations for habits and their completions.
    """

    def __init__(self, session: Session):
        """
        Initialize the HabitManager with a SQLAlchemy session.
      
        :param session: An active SQLAlchemy session.
        """
        self.session = session

    def create_habit(self, name: str, periodicity: str, description: str, creation_date: datetime = None) -> Habit:
        """
        Create a new habit and save it to the database.
        
        :param name: Name of the habit.
        :param periodicity: 'daily', 'weekly', or 'monthly'.
        :param description: Optional description of the habit.
        
        :return: The created Habit object.
        """
        habit = Habit(
            name=name,
            periodicity=periodicity,
            description=description,
            creation_date=datetime.now()
        )
        self.session.add(habit)
        self.session.commit()
        return habit


    def delete_habit(self, habit):
        pass

    # maybe not needed and will be removed later
    def rename_habit(self, old_name, new_name):
        pass


    def list_all_habits(self):
        pass


    def mark_habit_completed(self, habit):
        pass