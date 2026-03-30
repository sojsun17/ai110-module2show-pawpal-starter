# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
    Your initial UML design models PawPal+ with four core classes and clear responsibilities:

   -  Task represents an individual care item, storing what to do, when it is due, how long it takes, its priority, and whether it is complete. It includes mark_complete() to update status.
   -  Pet represents each animal, with identity details and a collection of tasks. It includes add_task() to attach tasks to that pet.
  -   Owner represents the user who manages one or more pets.
  -   Scheduler acts as the system’s coordinator, managing pets and their tasks through methods to add pets, gather all tasks, filter upcoming tasks, and check scheduling conflicts.

- What classes did you include, and what responsibilities did you assign to each?
    My initial UML design followed a hierarchical structure: an Owner acts as the top-level container, a Pet represents the individual animal, and a Task serves as the granular unit of work. 
- What classes did you include, and what responsibilities did you assign to each?

    - Task: Responsible for holding activity data like duration, priority, and completion status.- Pet: Responsible for storing pet-specific metadata (species, age) and maintaining its own list of assigned tasks.
    - Owner: Acts as the data entry point, managing a collection of multiple pets.
    - Scheduler: Functioning as the "Brain," this class is responsible for aggregating tasks across all pets, sorting them chronologically, and identifying potential timing conflicts.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
    Yes, my design evolved slightly during the skeleton implementation to improve data handling and reliability
- If yes, describe at least one change and why you made it.
    - One specific change was the decision to use Python Dataclasses for the Task, Pet, and Owner objects. Originally, I considered standard classes, but switching to dataclasses allowed for a much cleaner implementation of the logic layer by automatically handling initialization and providing a readable string representation (repr) for debugging. Additionally, I shifted the add_pet logic into the Scheduler class to centralize how the "Brain" accesses data across the entire system, rather than having the Scheduler reach into a separate Owner object constantly

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
    The scheduler considers chronological time (due time), task duration (to prevent physical overlaps), and task priority (low, medium, high) .
- How did you decide which constraints mattered most?
    Time and duration were prioritized as "hard" constraints because a pet cannot physically be in two places at once (e.g., a walk and a bath at 10:00 AM) . Priority was treated as a "soft" constraint to help the owner decide which tasks to focus on during busy periods.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
    The scheduler uses a "Simple & Readable" conflict detection algorithm that checks every task against every other task (O(P x T) complexity) rather than a more complex interval-tree approach .
- Why is that tradeoff reasonable for this scenario?
    For a single household with a few pets, the performance difference is measured in microseconds . Choosing readability makes the code much easier for a human to maintain and debug without losing any noticeable speed .

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
    I used AI for architectural brainstorming (UML drafting), writing algorithmic logic (the time-to-minutes conversion), and automated testing to verify the backend.
- What kinds of prompts or questions were most helpful?
    Prompts that asked for comparisons between different code versions (e.g., "simple vs efficient") were the most helpful for understanding design choices .

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
    When generating tests, the AI initially provided code that forgot to include the priority argument in the Task constructor.
- How did you evaluate or verify what the AI suggested?
    I ran pytest, identified the TypeError, and manually corrected the test code to match my pawpal_system.py requirements.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
    I tested chronological sorting (ensuring 08:00 comes before 18:00), conflict detection (blocking overlapping tasks), and task completion status.
- Why were these tests important?
    These tests ensure that the "Brain" of the app is reliable; without them, a pet owner might receive a broken schedule that misses important care activities .

**b. Confidence**

- How confident are you that your scheduler works correctly?
    I am very confident (5/5 stars) because the core algorithms are verified by an automated test suite that covers the most common user errors.
- What edge cases would you test next if you had more time?
    I would test tasks that wrap around midnight (e.g., 11:30 PM to 12:30 AM) and how the system handles multiple pets having identical task times simultaneously.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
    I am most satisfied with the integration between the UI and the Logic Layer. Seeing a real-time "Conflict Warning" appear in Streamlit based on my Python class logic was a major win.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
    I would fully implement the Recurring Task Logic so that "Daily" tasks automatically populate a new calendar entry for the next day as soon as they are checked off .

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
    I learned that being the "Lead Architect" means I am responsible for the context; AI is a powerful "senior dev" partner, but it only produces high-quality work when I provide clear constraints and verify its output against my system design.
