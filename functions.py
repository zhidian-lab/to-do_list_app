FILE_NAME = "to-dos.txt"
def get_action():
    with open(FILE_NAME, 'r') as file:
        print(file.readlines)
get_action()