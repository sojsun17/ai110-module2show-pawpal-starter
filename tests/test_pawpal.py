import pytest
from pawpal_system import Task, Pet

def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    # Create a dummy task
    task = Task(
        id=1, 
        description="Evening Feeding", 
        due_time="18:00", 
        duration_mins=10, 
        priority="high"
    )
    
    # Check initial status
    assert task.is_completed is False
    
    # Perform action
    task.mark_complete()
    
    # Verify change
    assert task.is_completed is True

def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    # Create a pet
    my_pet = Pet(name="Mochi", species="Dog", age=2)
    
    # Check initial task count
    assert len(my_pet.tasks) == 0
    
    # Create and add a task
    new_task = Task(
        id=2, 
        description="Brush Fur", 
        due_time="19:00", 
        duration_mins=15, 
        priority="low"
    )
    my_pet.add_task(new_task)
    
    # Verify the count increased
    assert len(my_pet.tasks) == 1
    assert my_pet.tasks[0].description == "Brush Fur"