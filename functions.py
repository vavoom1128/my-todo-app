FILEPATH = 'todos.txt'

def get_todos(filepath='todos.txt'):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Read a to_do items list in the text file."""
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)

if __name__ == '__main__':
    print('Hello')
    print(get_todos())
