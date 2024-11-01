FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Define a filepath of reading file, default todos.txt """
    with open(filepath, 'r') as file_function:
        todos_function = file_function.readlines()
    return todos_function


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print('Hello from functions!')
    print(__name__)