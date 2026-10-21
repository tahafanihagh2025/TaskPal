import sqlite3, csv, os
import view_tasks, progress_navigation

def delete_complete_task():
    """The delete_complete_task function is in charge of either marking a task as completed or deleting a task."""

    # Checking if any new tasks are available or not
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""SELECT ID FROM Tasks;""")
    any_task = my_cur.fetchall()

    if not any_task:
        print("No tasks available!")
        return
    else:
        pass

    my_conn.commit()
    my_conn.close()

    view_tasks.view_task()

    # Delete or Complete Choice
    while True:
        choice = input("\nWould you like to mark a task as Completed or simply Delete it (C: Complete / D: Delete)? ").strip().lower()
        print("")
        if choice not in ['c', 'd']:
            print("Not included, Try again!")
            continue
        else:
            # Delete the task
            if choice == "d":
                progress_navigation.word_progress("You're about to Delete a task...")
                try:
                    id_choice = int(input("Enter the task ID which you'd like to Delete: "))
                except ValueError as e:
                    print(f"Not included, Try again! | {e}\n")
                else:
                    my_conn = sqlite3.connect("taskpal_db.db")
                    my_cur = my_conn.cursor()
                
                    my_cur.execute("""DELETE FROM Tasks WHERE ID = ?;""", (id_choice,))

                    print("")

                    if my_cur.rowcount != 0:
                        progress_navigation.word_progress(f"Task {id_choice} deleted successfully!")
                        my_conn.commit()
                        my_conn.close() 
                        break
                    else:
                        progress_navigation.word_progress("No such task available!")
                    break  

            else:
                # Complete the task
                progress_navigation.word_progress("You're about to Complete a task...")
                try:
                    id_choice = int(input("Enter the task ID which you'd like to Complete: "))
                except ValueError as e:
                    print(f"Not included, Try again! | {e}\n")
                else:
                    my_conn = sqlite3.connect("taskpal_db.db")
                    my_cur = my_conn.cursor()

                    my_cur.execute("""SELECT * FROM Tasks WHERE ID = ?;""", (id_choice,))
                    task = my_cur.fetchall()

                    # Logging the completed tasks into a csv file
                    if len(task) != 0:
                        with open("completed_tasks.csv", "a", newline="", encoding="utf-8") as f:
                            csv_writer = csv.writer(f)

                            csv_writer.writerow(
                                [
                                    task[0][0], task[0][1], task[0][2],task[0][3], task[0][4], task[0][5], task[0][6], task[0][7]
                                ]
                            )
                            print("")

                        # Deleting a completed task from Database
                        my_cur.execute("""DELETE FROM Tasks WHERE ID = ?;""", (id_choice,))
                        
                        if my_cur.rowcount != 0:
                            progress_navigation.word_progress(f"Task ({task[0][0]}: {task[0][1]}) completed successfully!")
                            my_conn.commit()
                            my_conn.close()
                            os.system("start completed_tasks.csv")
                            break
                    else:
                        print("No such task available")
                        print("")
                        break              
