import os, time, dotenv
import ui, create_db, add_tasks, delete_complete_tasks, edit_tasks, view_tasks, ai_task, progress_navigation

def main():
    """The main function manages the whole program and dependencies."""
    ui.show_dashboard()
    time.sleep(1)

    progress_navigation.brick_progress()
    create_db.create_table()
    dotenv.load_dotenv()
    
    print("TaskPal Initialized Successfully!\n")
    progress_navigation.general_update()

    progress_navigation.brick_progress()

    choice = ""

    while choice != "0":
        choice = input("What would you like to do? ")

        os.system("cls")

        ui.show_dashboard()

        if choice == "1":
            time.sleep(0.5)
            progress_navigation.word_progress("Add a Task...")

            task_info = add_tasks.set_task()
            add_tasks.commit_task(task_info)

            progress_navigation.arrow_progress()

        elif choice == "2":
            time.sleep(0.5)
            progress_navigation.word_progress("Complete OR Delete a Task...")

            delete_complete_tasks.delete_complete_task()

            progress_navigation.arrow_progress()

        elif choice == "3":
            time.sleep(0.5)
            progress_navigation.word_progress("Edit a Task...")

            edit_tasks.edit_task()
        
            progress_navigation.arrow_progress()

        elif choice == "4":
            time.sleep(0.5)
            progress_navigation.word_progress("View Tasks...")

            view_tasks.view_task()

            progress_navigation.arrow_progress()

        elif choice == "5":
            time.sleep(0.5)
            progress_navigation.word_progress("AI Assistant...")

            ai_task.ai_prioritize()

            progress_navigation.arrow_progress()

        elif choice == "0":
            choice = "0"
            time.sleep(0.5)
            os.system("cls")
            progress_navigation.word_progress("Goodbye!")
        else:
            progress_navigation.word_progress("Not included, Try again!")
            time.sleep(0.5)

if __name__ == "__main__":
    main()
