from dataclasses import dataclass, field
from typing import List, Tuple
from datetime import datetime

@dataclass
class Task:
    """Sets the task status to completed."""
    id: int
    description: str
    due_time: str 
    duration_mins: int
    priority: str 
    frequency: str = "Once"
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Updates the task status to completed."""
        self.is_completed = True

@dataclass
class Pet:
    """Appends a new task to the pet's task list."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a care task to the pet's internal task list."""
        self.tasks.append(task)

@dataclass
class Owner:
    """Registers a new pet profile under the owner's management."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Gathers every task from every registered pet into a unified list."""
        self.pets.append(pet)

class Scheduler:
    def __init__(self):
        """"Initializes the scheduler with an empty list of pets."""
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the scheduler's tracking system."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Tuple[str, Task]]:
        """Aggregates all tasks from every registered pet into a single list of tuples"""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks

    def get_upcoming_tasks(self) -> List[Tuple[str, Task]]:
        """Returns a chronologically sorted list of all scheduled tasks."""
        tasks = self.get_all_tasks()
        # Sorts by the HH:MM string
        return sorted(tasks, key=lambda x: x[1].due_time)

    def check_conflicts(self, new_task: Task) -> bool:
        """Determines if a proposed task overlaps with existing appointments"""
        # Placeholder for conflict logic
        return False