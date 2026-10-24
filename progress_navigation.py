import time, sqlite3, csv, datetime

def brick_progress():
    """Brick Completion Animation"""
    for _ in range(40):
        print("=", end="", flush=True)
        time.sleep(0.01)
    print("")


def word_progress(sentence):
    """Word Completion Animation"""
    for char in sentence:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("")


def general_update():
    """
    The general_update function is in charge of providing an overview of 
    how many uncompleted tasks are available, how many completed tasks have been done and 
    categorizing the uncompleted tasks into 3 main sections of significance.
    """
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""SELECT * FROM Tasks;""")
    update = my_cur.fetchall()

    my_cur.execute("""SELECT priority FROM Tasks;""")
    priority = my_cur.fetchall()

    high_count, medium_count, low_count = 0, 0, 0
    for p in priority:
        if p[0] == 1:
            high_count += 1
        elif p[0] == 2:
            medium_count += 1
        else:
            low_count += 1

    my_conn.commit()
    my_conn.close()

    try:
        with open("completed_tasks.csv", "r", newline="", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            task_count = len(list(csv_reader)) - 1
    except:
        pass
   
    print(f"- You currently have {len(update)} uncompleted tasks available!")

    try:
        print(f"+ You've completed {task_count} tasks so far!\n")
    except:
        pass
    
    print(
    f"*1. You've got {high_count} tasks with HIGH priority\n"
    f"*2. You've got {medium_count} tasks with MEDIUM priority\n"
    f"*3. You've got {low_count} tasks with LOW priority\n\n"
    "(1. Add a Task | 2. Complete OR Delete a Task | 3. Edit a Task | 4. View Tasks | 5. AI Assistant)"
    )


def order_by_priority():
    """
    
    """
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""SELECT ID FROM Tasks;""")
    any_task = my_cur.fetchall()

    if not any_task:
        print("No tasks available!")
        return
    else:
        pass

    my_cur.execute("""SELECT ID, name, priority FROM Tasks
                    ORDER BY priority ASC, status DESC, estimatedTime ASC
    ;""")
    prioritized = my_cur.fetchall()

    my_conn.commit()
    my_conn.close()

    word_progress("ID | Name | Priority (1 - 3)")
    for task in prioritized:
        word_progress(f"{task[0]} | {task[1]} | {task[2]}")


def csv_practice():
    with open("example.csv", "r", newline="", encoding="utf-8") as file:
        csv_data = csv.reader(file)

        # sex_lst = []
        # for line in csv_data:
        #     if line[4] in ["Male", "Female"]:
        #         sex_lst.append(line[4])

        # print(sex_lst.count("Male"))
        # print(sex_lst.count("Female"))
        # print(len(sex_lst))
