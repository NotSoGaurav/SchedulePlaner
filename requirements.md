# Functional and Non-Functional Requirements
Functional Requirements (FR)
The project is structured around three major functional modules: Data Modeling, Management/CRUD, and Automation/Reporting.

    A. Data Modeling
        (1) The system must correctly model academic entities using Python OOP  
            classes (Course, Task).

        (2) Tasks must support fields for Name, Course association, Estimated 
            Time (in minutes), Priority (1-3), Deadline, and Completion Status.

    B. Management (CRUD)
        (1) The user must be able to Add, View, and Remove Courses and Tasks 
            using simple serial number identifiers for selection.

        (2) Input for task time must accept flexible units (Minutes, Hours, Days) 
            and correctly convert them to a single internal unit (minutes).

     C. Automation and Reporting
        (1) The system must generate a daily schedule by prompting the user for a 
            study time range (e.g., 9:00 AM - 1:00 PM).

        (2) The schedule must be sorted using a dual-criteria algorithm: Priority 
           (1-3, Ascending) then Time Needed (Shortest first).

        (3) The system must calculate and display overall project progress as a 
           percentage of estimated total time completed.

        (4) The "View All Tasks" feature must display data in a clean, delimited 
           list format, showing all relevant task properties.

# Non-Functional Requirements (NFR)
    I. Usability
        # The command-line interface must be simple and consistent, relying 
           solely on serial numbers (1, 2, 3...) for all user selections and modifications.

    II. Error Handling
        # The system must prevent application crashes by validating all 
          numerical and time format inputs, providing meaningful error messages to guide the user.
  
    III. Reliability
        # All user data must be automatically saved to a persistent file 
          (planner.json) upon exiting the application, ensuring that the state is not lost between sessions.

    IV. Maintainability
        # The codebase must adhere to a modular structure using distinct, 
          well-defined classes (Task, Course, Planner) to ensure logical separation of concerns and ease of future updates.