

# src/models.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Habit(Base):
    """
    a single habit defined by the user.
    """
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    periodicity = Column(String, nullable=False)  # "daily", "weekly" or "monthly"
    creation_date = Column(DateTime, default=datetime.now)

    # One-to-many relationship with Completion
    completions = relationship("Completion", back_populates="habit", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Habit id={self.id} name='{self.name}' periodicity={self.periodicity}>"


class Completion(Base):
    """
    Represents a single completion event for a habit.
    """
    __tablename__ = "completions"

    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)

    # Reference to the habit
    habit = relationship("Habit", back_populates="completions")

    def __repr__(self):
        return f"<Completion id={self.id} habit_id={self.habit_id} date={self.date.date()}>"
