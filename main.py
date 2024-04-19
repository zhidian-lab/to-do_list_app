todos = []
# def write_todos(args):
#     """args: todos"""
#     todos.append(input('please enter a todo: '))
#     while True:
#         todo = input("Enter a todo: ")
#         todos.append(todo)
# print(help(write_todos))
ranking = ['John', 'Sen', 'Lisa']
x = input('Enter a name: ')
for index, item in enumerate(ranking):
    if item == x:
        print(index + 1)
import time