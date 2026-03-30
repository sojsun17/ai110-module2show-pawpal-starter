import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

# 1. Check if 'owner' exists in the vault (session_state)
if "owner" not in st.session_state:
    # 2. If not, create the primary Owner and Scheduler instances
    st.session_state.owner = Owner(name="Jordan")
    st.session_state.scheduler = Scheduler()
    
    # 3. Create a default pet so the app isn't empty on first load
    default_pet = Pet(name="Mochi", species="dog", age=2)
    
    # 4. Register the pet to both the Owner and the Scheduler
    st.session_state.owner.add_pet(default_pet) [cite: 14-15]
    st.session_state.scheduler.add_pet(default_pet) [cite: 20-21]
    
    # Optional: Keep track of which pet is currently selected in the UI
    st.session_state.current_pet = default_pet

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    # 1. Create a real Task object using your class logic [cite: 7-8]
    new_task = Task(
        id=len(st.session_state.scheduler.get_all_tasks()) + 1,
        description=task_title,
        due_time="12:00",  # Placeholder: we can add a time picker later
        duration_mins=int(duration),
        priority=priority
    )
    
    # 2. Add the task to the pet in your scheduler [cite: 12-13, 17-18]
    # We'll use the first pet in the list for this demo
    if st.session_state.scheduler.pets:
        target_pet = st.session_state.scheduler.pets[0]
        target_pet.add_task(new_task)
        st.success(f"Added '{task_title}' to {target_pet.name}'s schedule!")
    else:
        st.error("No pets found! Please add a pet first.")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    # 1. Access the scheduler from the 'vault' (session state)
    scheduler = st.session_state.scheduler
    
    # 2. Call your actual sorting logic 
    upcoming_tasks = scheduler.get_upcoming_tasks()
    
    if not upcoming_tasks:
        st.info("No tasks scheduled yet. Add some tasks above to see your plan!")
    else:
        st.subheader("🗓️ Today's Optimized Care Plan")
        
        # 3. Prepare the data for a clean table display
        formatted_schedule = []
        for pet_name, task in upcoming_tasks:
            formatted_schedule.append({
                "Time": task.due_time,
                "Pet": pet_name,
                "Task": task.description,
                "Priority": task.priority,
                "Duration": f"{task.duration_mins} mins"
            })
        
        # 4. Display the results in a professional table
        st.table(formatted_schedule)
        
        st.success("Schedule generated successfully based on chronological order!")
