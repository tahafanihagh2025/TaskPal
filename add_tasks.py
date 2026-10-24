import sqlite3, datetime

def set_task():
    """
    The set_task function is in charge of getting the fundamental info 
    and details of a new task from the user.
    """
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

    creation_time = datetime.datetime.now().strftime("%H:%M:%S")
    creation_date = datetime.datetime.now().strftime("%Y/%m/%d")

    task_created_at = f"{creation_time} | {creation_date}"

    # input due date validation
    while True:
        try:
            due_date = input(f"6. Set a due date for {task_name} (ex. day/month/year): ").strip()
            x = due_date.split('/')

            if 1 <= int(x[0]) <= 31 and 1 <= int(x[1]) <= 12 and len(x[2]) == 4:
                task_due_date = datetime.date(int(x[2]), int(x[1]), int(x[0]))
                if task_due_date < datetime.date.today():
                    print(f"We're already passed {task_due_date}\n")
                    continue
                else:
                    task_due_date = datetime.date(int(x[2]), int(x[1]), int(x[0]))
            else:
                print("Undefined date!\n")
                continue
        except:
            pass
        else:
            break

    # input due time validation
    while True:
        try:  
            due_time = input(f"7. Set a due time (Reminder) for {task_name} (ex. 10:25, 14:30, 15:00): ").strip()
            y = due_time.split(':')

            if 1 <= int(y[0]) <= 24 and y[1] in [str(minute) if minute >= 10 else '0' + str(minute) for minute in range(0, 61)]:
                task_due_time = datetime.time(int(y[0]), int(y[1]))
                if task_due_date == datetime.date.today() and task_due_time <= datetime.datetime.now().time():
                    print(f"We're already passed {task_due_time}\n")
                    continue
                else:
                    task_due_time = datetime.time(int(y[0]), int(y[1]))
            else:
                print("Undefined time!\n")
                continue
        except:
            pass
        else:
            break

    task_due = f"{task_due_time} | {task_due_date}"

    return task_name, task_description, task_estimated_time, task_priority, task_status, task_created_at, task_due


def commit_task(task_info):
    """The commit_task function is in charge of receiving the given data about 
    a task provided by a user and storing it in the Tasks table and taskpal_db.db Databse."""
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    # Inserting the data from set_task function into the Database
    my_cur.execute("""INSERT INTO Tasks (name, description, estimatedTime, priority, status, createdAt, dueDate)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (*task_info,))

    my_conn.commit()
    my_conn.close()

    print(f"\nNew task {my_cur.lastrowid} added successfully!")
