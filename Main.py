import datetime as dt
import json
import os
import uuid

DATA_FILE = "planner.json"
TIME_FMT = '%I:%M %p'

class Task:
    def __init__(self, n, c, t, p, d, id=None, done=False):
        self.id = str(uuid.uuid4()) if not id else id
        self.name, self.course, self.time, self.priority = n, c, t, p
        self.deadline, self.completed = d, done
    def to_dict(self): return self.__dict__
    @staticmethod
    def from_dict(d):
        return Task(d['name'], d['course'], d['time'], d['priority'], d['deadline'], d['id'], d['completed'])

class Course:
    def __init__(self, n, tasks=None):
        self.name = n
        self.tasks = tasks or []
    def to_dict(self):
        return {'name': self.name, 'tasks': [t.to_dict() for t in self.tasks]}
    @staticmethod
    def from_dict(d):
        return Course(d['name'], [Task.from_dict(t) for t in d['tasks']])

class Planner:
    def __init__(self):
        self.courses = {}
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f: data = json.load(f)
                self.courses = {c['name']: Course.from_dict(c) for c in data.get('courses', [])}
                print(f"\nLoaded {len(self.courses)} courses.")
            except: print("\nError loading data. Starting fresh.")

    def save(self):
        data = {'courses': [c.to_dict() for c in self.courses.values()]}
        with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)
        print("\nSaved planner data.")

    def get_tasks(self, pending=True):
        all_tasks = [t for c in self.courses.values() for t in c.tasks]
        return [t for t in all_tasks if not pending or not t.completed]

    def add_course(self, name):
        if name not in self.courses:
            self.courses[name] = Course(name); print(f"Added '{name}'.")
        else: print(f"'{name}' exists.")

    def remove_course(self, name):
        if input(f"Type 'CONFIRM' to delete '{name}': ").upper() == 'CONFIRM':
            del self.courses[name]; print(f"Removed '{name}'.")
        else: print("Removal cancelled.")

    def add_task(self, c_name, n, t_min, p, d):
        self.courses[c_name].tasks.append(Task(n, c_name, t_min, p, d)); print(f"Task '{n}' added.")

    def clear(self):
        if input("Type 'YES' to clear ALL tasks: ").upper() == 'YES':
            for c in self.courses.values(): c.tasks = []
            print("Cleared all tasks.")

    def get_progress(self):
        tasks = self.get_tasks(pending=False);
        if not tasks: return 0.0, 0, 0
        total = sum(t.time for t in tasks)
        done = sum(t.time for t in tasks if t.completed)
        return (done/total)*100, done, total

    def get_schedule(self, available_mins, start_time_str):
        tasks = sorted(self.get_tasks(), key2=lambda t: (t.priority, t.time))
        schedule, time_spent = [], 0
        try: current_time = dt.datetime.strptime(start_time_str, TIME_FMT)
        except: return []

        for t in tasks:
            if time_spent + t.time <= available_mins:
                start_str = current_time.strftime(TIME_FMT)
                end_time = current_time + dt.timedelta(minutes=t.time)
                end_str = end_time.strftime(TIME_FMT)
                schedule.append((t.name, t.course, start_str, end_str))
                time_spent += t.time
                current_time = end_time
        return schedule

def get_input(prompt, type_func=str, valid_check=lambda x: True, error="Invalid input."):
    while True:
        try:
            val = type_func(input(prompt).strip())
            if valid_check(val): return val
            else: print(error)
        except ValueError: print("Please enter a valid number/value.")

def cli_interface():
    p = Planner(); courses = list(p.courses.keys())
    while True:
        print("\n" + "="*40); print("  📚 Smart Study Planner Menu 📊"); print("="*40)
        menu = ["Edit Courses (Add/Remove)", "Add Task", "View All Tasks", "Generate Schedule",
                "Mark Complete", "View Progress", "Clear All Tasks", "Exit and Save"]
        for i, item in enumerate(menu): print(f"{i+1}. {item}")
        choice = get_input("Choice (1-8): ", int, lambda x: 1 <= x <= 8, "Invalid choice.")

        if choice == 1: # Edit Courses
            while True:
                print("\nCourses:");
                if not courses: print("  (None)")
                for i, n in enumerate(courses): print(f"{i+1}. {n}")
                sub = get_input("1. Add, 2. Remove (Num), 3. Back: ", int, lambda x: 1<=x<=3)
                if sub == 3: break
                elif sub == 1: p.add_course(get_input("Name: ")); courses = list(p.courses.keys())
                elif sub == 2 and courses:
                    n = get_input("Remove #:", int, lambda x: 1<=x<=len(courses))
                    p.remove_course(courses[n-1]); courses = list(p.courses.keys())
                elif sub == 2: print("No courses.")
        elif choice == 2: # Add Task
            if not courses: print("Add a course first."); continue
            for i, n in enumerate(courses): print(f"{i+1}. {n}")
            c_idx = get_input("Course #:", int, lambda x: 1<=x<=len(courses)); c_name = courses[c_idx-1]
            n = get_input("Task Name: "); d = get_input("Deadline: ")
            unit = get_input("Time Unit (1=Min, 2=Hr, 3=Day): ", int, lambda x: 1<=x<=3)
            amount = get_input("Time Amount: ", int, lambda x: x>0)
            t_min = amount * [1, 60, 1440][unit-1]
            prio = get_input("Priority (1-3): ", int, lambda x: 1<=x<=3)
            p.add_task(c_name, n, t_min, prio, d)
        elif choice == 3: # View All Tasks
            tasks = p.get_tasks(pending=False)
            if not tasks: print("No tasks."); continue
            print("\n" + "="*77); print(f"| {'COURSE':<15} | {'TASK':<35} | {'DEADLINE':<10} | {'PROGRESS':<8} |")
            print("="*77)
            for t in tasks:
                prog = "✅ Done" if t.completed else f"P{t.priority}"
                print(f"| {t.course[:15]:<15} | {t.name[:35]:<35} | {t.deadline:<10} | {prog:^8} |")
            print("="*77)
        elif choice == 4: # Generate Schedule
            tasks = p.get_tasks(); 
            if not tasks: print("No pending tasks."); continue
            range_str = get_input("Time Range (H:MM AM/PM-H:MM AM/PM, e.g., 9:00 AM - 1:00 PM): ")
            parts = [s.strip() for s in range_str.split('-', 1)]
            if len(parts) != 2: print("Bad format."); continue
            try:
                start, end = dt.datetime.strptime(parts[0], TIME_FMT), dt.datetime.strptime(parts[1], TIME_FMT)
                diff = end - start;
                if diff.total_seconds() < 0: diff += dt.timedelta(days=1)
                daily_mins = int(diff.total_seconds() / 60)
            except: print("Bad time value."); continue
            schedule = p.get_schedule(daily_mins, parts[0])
            print("\n--- SCHEDULE ---")
            if not schedule: print("No tasks scheduled.")
            for n, c, s, e in schedule: print(f"[{s} - {e}] -> {c}: {n}")
            print("----------------")
        elif choice == 5: # Mark Complete
            tasks = p.get_tasks();
            if not tasks: print("No pending tasks."); continue
            for i, t in enumerate(tasks): print(f"{i+1}. [P{t.priority}] {t.course} - {t.name}")
            t_idx = get_input("Complete #: ", int, lambda x: 1<=x<=len(tasks))
            tasks[t_idx-1].completed = True; print(f"'{tasks[t_idx-1].name}' marked complete.")
        elif choice == 6: # View Progress
            prog, done, total = p.get_progress()
            print(f"\nProgress: {prog:.2f}% ({done} of {total} mins complete).")
        elif choice == 7: # Clear All Tasks
            p.clear()
        elif choice == 8: # Exit and Save
            p.save(); return

if __name__ == "__main__":
    cli_interface()