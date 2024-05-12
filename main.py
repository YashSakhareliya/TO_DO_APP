# get todos list
#from function import get_todos,write_todos
import function
import time

cur_time = time.strftime("IS NOW, %d %b - %Y, %I:%M:%S %p")
print(cur_time)

while True:
    User_action = input("Type add,show,edit,complete,exit: ")
    User_action = User_action.strip() # strip() for removing space

    if User_action.startswith("add"):
        todo = User_action[4:] + '\n'

        todos = function.get_todos("todos.txt")     #call function get todolist

        todos.append(todo)


        function.write_todos(todos)

    elif User_action.startswith("show"):

        todos = function.get_todos("todos.txt")

        for index, todo in enumerate(todos):    #enumerate for give number of todos
            todo = todo.strip('\n')
            print(f"{index+1} - {todo}")

    elif User_action.startswith("edit"):

        try:
            number = int(User_action[5:])
            number = number-1

            todos = function.get_todos("todos.txt")

            New_todo = input("Enter your new todo: ")
            todos[number] = New_todo + "\n"

            function.write_todos(todos)

        except ValueError:
            print("Invalid command ")
            continue

    elif User_action.startswith("complate"):
        try:
            number = int(User_action[9:])

            todos = function.get_todos("todos.txt")

            index = number - 1

            Remove_todo =todos[index].strip('\n')
            todos.pop(index)

            function.write_todos(todos)

            print(f"Completed {Remove_todo}")
        except IndexError:
            print("No item that index")
            continue

    elif User_action.startswith("exit"):
        break

    else:
        print("Sorry, I didn't understand")


