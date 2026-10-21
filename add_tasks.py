import sqlite3, functools, datetime

# def add_task(func):

#     @functools.wraps(func)
#     def wrapper_set_task(*args, **kwargs):
#         func(*args, **kwargs)

#     def wrapper_commit_task(*args, **kwargs):
#         func(*args, **kwargs)

#     return wrapper_set_task, wrapper_commit_task

# @add_task
def set_task():
    """The set_task function is in charge of getting the fundamental info 
    and details of a new task from the user."""
    task_name = input("1. Create a name for your task: ")
    task_description = input(f"2. Proivde a brief description of {task_name}: ")

    # input estimation time validation
    while True:
        try:
            task_estimated_time = int(input(f"3. How much time do you think it'll take you to accomplish (ex. 25 minutes)? "))
        except ValueError as e:
            print(f"Not included, Try again! | {e}\n")
        else:
            break

    # input priority validation
    while True:
        try:
            task_priority = int(input(f"4. Set a priority for {task_name} (1. High / 2. Medium / 3. Low): "))
            if task_priority not in [1, 2, 3]:
                print(f"{task_priority} Out of range (1 - 3), Try again!\n")
                continue
        except ValueError as e:
            print(f"Not included, Try again! | {e}\n")
        else:
            break

    # input completion status validation
    while True:
        try:
            task_status = int(input("5. How much of it out of 100 has been done so far (ex. 45)? "))
            if task_status not in range(0, 101):
                print(f"{task_status} Out of range (0 - 100), Try again!\n")
                continue
        except ValueError as e:
            print(f"Not included, Try again! | {e}\n")
        else:
            break

    creation_time = datetime.datetime.now().strftime("%H:%M")
    creation_date = datetime.datetime.now().strftime("%Y/%m/%d")

    task_created_at = f"{creation_time} | {creation_date}"

    # input due date validation
    while True:
        try:
            due_date = input(f"6. Set a due date for {task_name} (ex. day/month/year): ").strip()
            x = due_date.split('/')
            task_due_date = datetime.date(int(x[2]), int(x[1]), int(x[0]))
        except ValueError as e:
            print(f"Not included, Try again! | {e}\n")
        else:
            break

    # input due time validation
    while True:
        try:  
            due_time = input(f"7. Set a due time (Reminder) for {task_name} (ex. 10:25, 14:30, 15:00): ").strip()
            y = due_time.split(':')
            task_due_time = datetime.time(int(y[0]), int(y[1]))
        except ValueError as e:
            print(f"Not included, Try again! | {e}\n")
        else:
            break

    task_due = f"{task_due_time} | {task_due_date}"

    return task_name, task_description, task_estimated_time, task_priority, task_status, task_created_at, task_due

# @add_task
def commit_task(task_info):
    """The commit_task function is in charge of receiving the given data about 
    a task provided by a user and storing it in the Tasks table and taskpal_db.db Databse."""
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    # Inserting the data from set_task function into the Database
    my_cur.execute("""INSERT INTO Tasks (name, description, estimatedTime, priority, status, createdAt, dueDate)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (*task_info,))

    # Counting the number of remaining tasks
    my_cur.execute("""SELECT COUNT(ID) FROM Tasks;""")
    remaining_tasks = my_cur.fetchall()

    my_conn.commit()
    my_conn.close()

    print(f"\nNew task {my_cur.lastrowid} added successfully!\nYou currently have {remaining_tasks[0][0]} uncompleted tasks available!")


# class Task:
#     def __init__(self):
#         pass

#     def set_task(self):
#         self.name = input("1. Create a name for your task: ")
#         self.description = input(f"2. Proivde a brief description of {self.name}: ")
#         self.estimated_time = int(input(f"3. How much time do you think it'll take you to accomplish (ex. 25 minutes)? "))
#         self.priority = int(input(f"4. Set a priority for {self.name} | (1. High / 2. Medium / 3. Low): "))
#         self.status = int(input("5. How much of it has been done so far (ex. 10%)? "))
    
#         creation_time = datetime.datetime.now().strftime("%H:%M")
#         creation_date = datetime.datetime.now().strftime("%Y/%m/%d")
#         self.created_at = f"{creation_time} | {creation_date}"
    
#         custom_deadline = input(f"6. Set a deadline / due date for {self.name} (ex. day/month/year): ").strip()
#         x = custom_deadline.split('/')
#         self.deadline = datetime.date(int(x[2]), int(x[1]), int(x[0]))

#         return self.name, self.description, self.estimated_time, self.priority, self.status, self.created_at, self.deadline

#     def commit_task(self, task_info):
#         my_conn = sqlite3.connect("taskpal_db.db")
#         my_cur = my_conn.cursor()
        
#         my_cur.execute("""INSERT INTO Tasks (name, description, estimatedTime, priority, status, createdAt, dueDate)
#                         VALUES (?, ?, ?, ?, ?, ?, ?);
#         """, (*task_info,))

#         my_cur.execute("""SELECT COUNT(ID) FROM Tasks;""")
#         remaining_tasks = my_cur.fetchall()

#         print(f"\nNew task {my_cur.lastrowid} added successfully!\nYou currently have {remaining_tasks[0][0]} uncompleted tasks.")

#         my_conn.commit()
#         my_conn.close()

#     def __str__(self):
#         pass

#     def __repr__(self):
#         pass

# task = Task()
# task_info = task.set_task()
# task.commit_task(task_info)