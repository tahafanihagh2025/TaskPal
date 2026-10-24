import sqlite3
import add_tasks, view_tasks

def edit_task():
    """
    
    """
    allow_continue = view_tasks.view_task()
    
    if allow_continue:
        pass
    else:
        return
    
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    print("")
    
    while True:
        try:
            id_choice = int(input("Enter the task ID you'd like to Edit: "))
            my_cur.execute("""SELECT * FROM Tasks WHERE ID = ?;""", (id_choice,))
            if my_cur.fetchall():
                break
            else:
                print("No such task found, Try again!\n")
                continue
        except ValueError as e:
            print(f"No such task found, Try again! | {e}\n")

    edit_info = add_tasks.set_task()

    my_cur.execute("""UPDATE Tasks
                    SET name = ?,
                        description = ?, 
                        estimatedTime = ?, 
                        priority = ?, 
                        status = ?, 
                        createdAt = ?, 
                        dueDate = ?
                    WHERE ID = ?;
    """, (*edit_info, id_choice,))

    print(f"\nTask {id_choice} edited successfully!")

    my_conn.commit()
    my_conn.close()
