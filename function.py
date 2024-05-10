def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as File_local:
        todos_local = File_local.readlines()    # read file method using readlines for list
    return todos_local


def write_todos(todos_local,filepath="todos.txt"):
    with open(filepath, "w") as File:  # overwrite existing file with new list
        File.writelines(todos_local)

