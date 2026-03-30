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
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
