📚 Smart Study Planner (CLI) - VITyarthi Project Submission

This project is a robust, command-line interface (CLI) application built in Python that utilizes Object-Oriented Programming (OOP) to help students efficiently organize, prioritize, and schedule their study sessions. It functions as a complete time management system for academic workloads.

💻 Technologies/Tools Used

Primary Language: Python 3.13.7

    Core Concepts: Object-Oriented Programming (OOP), Data Structures (Lists, Dictionaries)

    Modules: datetime (for scheduling), json (for persistence), uuid (for unique IDs)

✨ Core Features

        - OOP Structure: Implemented with Course and Task classes for strong data encapsulation.

        - Priority Scheduling: Uses a smart algorithm that prioritizes tasks by Priority (High to Low) and then by Time Needed (Shortest first) to ensure efficient time-boxing.

        -Flexible Time Input: Allows users to define task durations in Minutes, Hours, or Days.

        -12-Hour Clock Support: Schedule generation uses the intuitive H:MM AM/PM format.

        -Data Persistence: Automatically saves all data to a local JSON file (planner.json) and loads it on startup.

    Usability: All interactions, including selection and modification, are handled via simple serial number input.

    Progress Tracking: Calculates overall study progress based on estimated time completed.

🚀 How to Run

    - Prerequisites
        Python 3.13.7

    - Execution

        Save the file: Save the provided code as study_planner.py.

    - Run from terminal:

        python study_planner.py

📋 Menu Options

    - The application presents a main menu with the following options:

        1. Edit Courses (Add/Remove)

        2. Add Task

        3. View All Tasks (Tabular format)

        4. Generate Schedule (Time-boxed plan)

        5. Mark Complete

        6. View Progress
 
        7. Clear All Tasks

        8. Exit and Save

📝 Project Documentation & Design Artifacts

    - File
    - Requirement
    - Description
    - statement.md
    - Problem Statement, Scope, Target Users, High-Level Features
    - Provides the executive summary of the project goals.
    - requirements.md
    - Functional & Non-Functional Requirements
    - Formal listing of all features and quality attributes (Usability, Reliability, Error   
      Handling).
    - design_artifacts.md
    - System Architecture, Workflow, UML Diagrams
    - Contains the visual and structural design documentation required for submission.
    - study_planner.py
    - Source Code
    - Complete, modular, and runnable Python implementation.