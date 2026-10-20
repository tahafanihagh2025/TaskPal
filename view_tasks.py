import sqlite3
import progress_navigation

def view_task():
    """The view_task function is in charge of providing the user with their remaining tasks available."""
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    # Checking if any new tasks are available or not
    my_cur.execute("""SELECT ID FROM Tasks;""")
    any_task = my_cur.fetchall()

    if not any_task:
        print("No tasks available!")
        return
    else:
        print(f"{len(any_task)} uncompleted tasks available!")

    my_conn.commit()
    my_conn.close()

    # Retrieving all tasks from Database
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""SELECT * FROM Tasks;""")
    all_tasks = my_cur.fetchall()

    my_conn.commit()
    my_conn.close()

    print("")

    for task in all_tasks:
        progress_navigation.word_progress(f"{task[0]}: {task[1]}")

    print("")

    # Accessing the tasks' details info
    while True:
        choice = input("Would you like to see more (Y / N)? ").strip().lower()
        if choice == "y":

            print("")

            # Priority setting
            for task in all_tasks:

                if task[4] == 1:
                    task_priority = "High"
                elif task[4] == 2:
                    task_priority = "Medium"
                else:
                    task_priority = "Low"

                print(  
                    f"TASK {task[0]} at a glance!\n\n"
                    f"ID: {task[0]}\n"
                    f"Name: {task[1]}\n"
                    f"Description: {task[2]}\n"
                    f"Estimated Time: {task[3]} minutes\n"
                    f"Priority: {task[4]} -> {task_priority}\n"

                    f"Completion Status: {task[5]} %\n"
                    f"Time of creation: {task[6]}\n"
                    f"Deadline: {task[7]}"
                )
                progress_navigation.brick_progress()
            break
        elif choice == "n":
            print("")
            progress_navigation.word_progress("All right, back to HOME...")
            break
        else:
            print(f"Not included, Try again!\n")
            continue
