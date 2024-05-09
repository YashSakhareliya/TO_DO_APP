# get todos list
def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as File_local:
        todos_local = File_local.readlines()    # read file method using readlines for list
    return todos_local


def write_todos(todos_local,filepath="todos.txt"):
    with open(filepath, "w") as File:  # overwrite existing file with new list
        File.writelines(todos_local)



while True:
    User_action = input("Type add,show,edit,complete,exit: ")
    User_action = User_action.strip() # strip() for removing space

    if User_action.startswith("add"):
        todo = User_action[4:] + '\n'

        todos = get_todos("todos.txt")     #call function get todolist

        todos.append(todo)


        write_todos(todos)

    elif User_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, todo in enumerate(todos):    #enumerate for give number of todos
            todo = todo.strip('\n')
            print(f"{index+1} - {todo}")

    elif User_action.startswith("edit"):

        try:
            number = int(User_action[5:])
            number = number-1

            todos = get_todos("todos.txt")

            New_todo = input("Enter your new todo: ")
            todos[number] = New_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Invalid command ")
            continue

    elif User_action.startswith("complate"):
        try:
            number = int(User_action[9:])

            todos = get_todos("todos.txt")

            index = number - 1

            Remove_todo =todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"Completed {Remove_todo}")
        except IndexError:
            print("No item that index")
            continue

    elif User_action.startswith("exit"):
        break

    else:
        print("Sorry, I didn't understand")


