import time
import functions
now = time.strftime("%Y-%b-%d, %H:%M:%S")    
print("It is:", now)

while True:
    user_action = input("Please type add, complete, edit, show or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:
        user_action = user_action[4:]
        functions.add_action(user_action)
    elif 'complete' in user_action:
        user_action = user_action[9:]
        to_dos = functions.get_action(user_action)
        new_to_dos = []
        for i, row in enumerate(to_dos):
            if i + 1 == user_action:
                continue
            new_to_dos.append(row)
        functions.overwrite_action(user_action)
    elif 'edit' in user_action:
        user_action = user_action[5:]
        new_action = input('Please update: ')
        new_action = new_action.strip()
        to_dos = functions.get_action(user_action)
        new_to_dos = []
        for i, row in enumerate(to_dos):
            if i + 1 == user_action:
                new_to_dos.append(new_action)
            else:
                new_to_dos.append(row)
        functions.overwrite_action(new_to_dos)
    elif 'show' in user_action:
        to_dos = functions.get_action(user_action)
        for i, row in enumerate(to_dos):
            print(f"{i + 1}-{row}")
    elif 'exit' in user_action:
        break
    else:
        print("Please enter correct command!")