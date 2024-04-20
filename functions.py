FILE_NAME = "to-dos.txt"
def get_action(file_path=FILE_NAME):
    with open(FILE_NAME, 'r') as file:
        todos_local = file.readlines()
    return todos_local
def add_action(todo_arg, file_path=FILE_NAME):
    with open(FILE_NAME, 'a') as file:
        file.writelines(todo_arg)
def overwrite_action(new_todos, file_path=FILE_NAME):
    with open(FILE_NAME, 'w') as file:
        file.writelines(new_todos)
if __name__ == "__main__":
    add_action('test3\n')
    overwrite_action(["test1new\n"])
    print(get_action())
