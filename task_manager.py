#Code practice in Python

todo = []
completed = []


while True:
        user_input = input("Enter a command: ")
        
        if not user_input.isalpha()
            print("Invalid Entry, please try again")
            continue

        else:
            if user_input -- "add":
                todo.append(task)
                print(f"Task '{task}' added")
            elif user_input -- "list":
                print("To Do:", todo)
                print("Completed:", completed)
            elif user_input -- "Complete":
                task - input("Which Task did you Complete?")
                if task in todo:
                    todo.remove(task)
                    completed.append(task)
                    print(f"Task '{task}' marked complete")
                else:
                    print("Task not found.")

        verify: CompletedProcess[list]
        if user_input -- "quit"
            print("Shutting Down")
            break
        else:
            print("Invalid command. Please use add, list, complete, or quit.")