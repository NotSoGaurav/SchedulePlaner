# Project Statement: Smart Study Planner

# Problem Statement
Students frequently face academic stress due to poor time allocation and difficulty prioritizing tasks across multiple subjects. Existing static to-do lists lack the intelligence to convert a course backlog into an executable, time-constrained daily plan. This project addresses the necessity for an automated, intelligent Command Line Interface (CLI) application that generates a time-boxed study schedule, thereby simplifying daily planning and boosting study efficiency.

# Objectives
The primary objectives for this foundational project are:

1. OOP Implementation: Demonstrate proficiency by modeling entities using modular Python classes (Course, Task, Planner).

2. Algorithm Design: Implement a non-trivial scheduling algorithm that    
prioritizes tasks based on both priority level and estimated time.

3. Usability & Persistence: Ensure data integrity (saving/loading data) and simplify user input through serial number indexing and validation.

4. Time Management Application: Apply the Python datetime module for accurate time calculation, supporting intuitive 12-hour AM/PM schedule output.

# Scope of the Project

The project is a console-based, command-line interface (CLI) application focused on core scheduling automation.
  # In Scope:

  (A) Data Management (CRUD): Full management of Courses and Tasks using serial number selection.

  (B) Scheduling Algorithm: Prioritization based on Priority (High to Low) then Time Needed (Shortest First).

  (C) Persistence: Reliable storage and retrieval of application state via JSON file management.

  (D) Reporting: Calculation of overall progress based on estimated total effort.

  # Out of Scope (Future Enhancements):

  (A) Graphical User Interface (GUI) or web integration.

  (B) Cloud storage or multi-user support.

  (C) External API integration (e.g., calendar services).

# Target Users
The primary target users are University and High School Students who:
     # Manage a heavy academic workload.

     # Require structured organization to convert assignments into daily 
       actionable time blocks.

     # Benefit from forced time-boxing to maintain focus.

# High-Level Features

#1 Course Management: Functions to add, list, and remove courses.

#2 Task Management: Captures essential metadata: name, flexible time (Min/Hr/  
   Day), priority, and deadline.

#3 Intelligent Scheduling: Automated schedule generation based on user-defined 
   available time and prioritization rules.

#4 Progress Reporting: Displays overall completion percentage.

#5 Reliable Persistence: Automatic saving and loading of all planner data.