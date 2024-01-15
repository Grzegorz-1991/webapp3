# from functions import get_todos, write_todos
import functions
import time


while True:
    now = f"Today is {time.strftime("%b %d %Y %H:%M:%S")}"
    print(now)

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('edit'):
        try:
            index_list = int(user_action[5:])
            index_list = index_list - 1

            todos = functions.get_todos()

            todo = input("Enter a new todo")
            todos[index_list] = todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Please enter a valid command (number for editing)')
            continue

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append(new_item)

        # new_todos = []
        new_todos = [item.strip('\n') for item in todos]

        todos = new_todos

        for indeks,one_todo in enumerate(todos, 1):
            print(f"{indeks}-{one_todo}")

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            index = number - 1
            removed = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {removed} was deleted from todos list."
            print(message)
        except IndexError:
            print('Enter a valid number of index')
            print(f'You have {len(todos)} items on list')
            continue
            
    elif user_action.startswith('exit'):
        break
    else:
        print("You entered an unknow command")

print("Bye!")