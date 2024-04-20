import time
import functions
now = time.strftime("%Y-%b-%d, %H:%M:%S")    
print("It is:", now)

while True:
    user_action = input("Please type add, complete, edit, show or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:
        user_action = user_action[4:]
        functions.add_action(f"{user_action}\n")

    elif 'complete' in user_action:
        index = int(user_action[9:])
        todos = functions.get_action(user_action)
        message = todos.pop(index - 1)
        message = message.strip("\n")
        functions.overwrite_action(todos)
        print(f"{message} is removed")

    elif 'edit' in user_action:
        index = int(user_action[5:])
        new_todo = input('Please update: ')
        new_todo = new_todo.strip() + "\n"
        todos = functions.get_action()
        new_todos = []
        new_todos[index - 1] = new_todo
        functions.overwrite_action(new_todos)

    elif 'show' in user_action:
        todos = functions.get_action(user_action)
        for i, row in enumerate(todos):
            row = row.strip("\n")
            print(f"{i + 1}-{row}")

    elif 'exit' in user_action:
        break

    else:
        print("Please enter correct command!")