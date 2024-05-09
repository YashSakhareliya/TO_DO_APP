while True:
    User_action = input("Type add,show,edit,complete,exit: ")
    User_action = User_action.strip()

    if User_action.startswith("add"):
        todo = User_action[4:] + '\n'

        with open("todos.txt", "r") as File:
            todos = File.readlines()

        todos.append(todo)


        with open("todos.txt", "w") as File:
            File.writelines(todos)

    elif User_action.startswith("show"):

        with open("todos.txt", "r") as File:
            todos = File.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index+1} - {todo}")

    elif User_action.startswith("edit"):

        try:
            number = int(User_action[5:])
            number = number-1

            with open("todos.txt", "r") as File:
                todos = File.readlines()

            New_todo = input("Enter your new todo: ")
            todos[number] = New_todo + "\n"

            with open("todos.txt",'w') as File:
                File.writelines(todos)
        except ValueError:
            print("Invalid command ")
            continue

    elif User_action.startswith("complate"):
        try:
            number = int(User_action[9:])
            with open("todos.txt", "r") as File:
                todos = File.readlines()
            index = number - 1

            Remove_todo =todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", "w") as File:
                File.writelines(todos)

            print(f"Completed {Remove_todo}")
        except IndexError:
            print("No item that index")
            continue

    elif User_action.startswith("exit"):
        break

    else:
        print("Sorry, I didn't understand")

