


import questionary
from .manager import HabitManager


class interface:
    """
    Command-line interface for interacting with the Habit Manager.
    """

    def __init__(self, manager: HabitManager):
        self.manager = manager

    def main_menu(self):
        while True:
            choice = questionary.select(
                "Main Menu:",
                choices=[
                    "Create Habit",
                    "Exit"
                ]
            ).ask()

            if choice == "Create Habit":
                self.prompt_create_habit()
            elif choice == "Exit":
                break

    def prompt_create_habit(self):
        """
        Ask the user for habit details and create the habit.
        """
        name = questionary.text("Enter habit name:").ask()
        if not name:
            print("❌ Habit name cannot be empty.")
            return

        description = questionary.text("Enter description (optional):").ask()

        periodicity = questionary.select(
            "Select periodicity:",
            choices=["daily", "weekly", "monthly"]
        ).ask()

        # Call manager to create the habit
        habit = self.manager.create_habit(
            name=name,
            description=description or None,
            periodicity=periodicity
        )

        print(f"✅ Habit '{habit.name}' created with ID {habit.id}.")


#@ToDo
# check the length of the habit name and description entered by the user
