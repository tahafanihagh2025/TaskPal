import time, sqlite3, csv

def brick_progress():
    """Brick Completion Animation"""
    for _ in range(40):
        print("=", end="", flush=True)
        time.sleep(0.01)
    print("")


def arrow_progress():
    """Arrow Completion Animation"""
    for _ in range(40):
        print(">", end="", flush=True)
        time.sleep(0.05)
    print("")


def bar_progress():
    pass


def word_progress(sentence):
    """Word Completion Animation"""
    for char in sentence:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("")


def is_task():
    """The is_task function checks if any new tasks are available or not."""
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""SELECT ID FROM Tasks;""")
    any_task = my_cur.fetchall()

    if not any_task:
        print("No tasks available!")
        return
    else:
        print(f"{len(any_task)} uncompleted tasks available!")

    my_conn.commit()
    my_conn.close()


def general_update():
    """The general_update function is in charge of providing an overview of 
    how many uncompleted tasks are available, how many completed tasks have been done and 
    categorizing the uncompleted tasks into 3 main sections of significance"""
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

    with open("completed_tasks.csv", "r", newline="", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        task_count = len(list(csv_reader))

    print(
        f"- You currently have {len(update)} uncompleted tasks available!\n"
        f"+ You've completed {task_count} tasks so far!\n\n"
        f"1. You've got {high_count} tasks with HIGH priority\n"
        f"2. You've got {medium_count} tasks with MEDIUM priority\n"
        f"3. You've got {low_count} tasks with LOW priority"
    )


def csv_practice():
    with open("completed_tasks.csv", "r", newline="", encoding="utf-8") as f:
        csv_reader = csv.reader(f)

        # for line in csv_reader:
        #     if line[1] in ["Claude", "Anthropic", "oop"]:
        #         print(line)

        # id_lst = []
        # for line in csv_reader:
        #     id_lst.append(line[1])
        # print(sorted(id_lst))

    with open("example.csv", "r", newline="", encoding="utf-8") as file:
        csv_data = csv.reader(file)

        sex_lst = []
        for line in csv_data:
            if line[4] in ["Male", "Female"]:
                sex_lst.append(line[4])

        print(sex_lst.count("Male"))
        print(sex_lst.count("Female"))
        print(len(sex_lst))
