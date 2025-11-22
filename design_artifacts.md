# System Architecture and Design Artifacts
        
   # System Architecture

     The Smart Study Planner follows a simple, robust layered architecture suitable for a standalone CLI application.

         Components:
                Presentation Layer (I/O): Handled by the cli_interface() and get_input() functions. This layer manages all user interaction, prompts, and output formatting (e.g., menus, tables).

                Business Logic Layer (Core Logic): Handled by the Planner class and its methods (e.g., get_schedule, get_progress). It contains the core academic domain knowledge, prioritization algorithms, and time calculation logic.

                Data Access Layer (Persistence): Handled by the save() and load() methods within the Planner class, which manages reading and writing data to the planner.json file.

    7. Design Diagrams

7.1 Process Flow / Workflow Diagram

This diagram outlines the primary user path for generating a daily schedule.

7.2 Class Diagram (UML)

This UML Class Diagram shows the key entities and their relationships, adhering to the OOP principles used in the implementation.

Key Relationships:

Composition (1:M): A Course object has multiple Task objects.

Aggregation (1:M): The central Planner object aggregates multiple Course objects.

7.3 Component Diagram (UML)

The component diagram illustrates the modular structure defined in the code, fulfilling the requirement for a modular design, even if compiled into one file.