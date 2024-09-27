#TO DO LIST
#ToDoList


def ToDolist():
    list = []
    print("This is a program that creates a to do list for you")
    print(f"\nWELCOME TO YOUR TO-DO-LIST\n")
    name = input("Greetings user what is your name?: ")
    while True:
        print(""" Press
        1 = adding To list
        2 = deleting From list
        3 = Viewing list""")
        choice = (input(f"\nWhat do you want to do: ")) # Be more direct -> "Enter a choice/number: "
        if choice == "1":
            user = input("Add your task: ")
            list.append(user)
            print(list)
        elif choice == "2":
            user = input("What task do you want to delete: ") #How do you know what is already in your list when choosing? Suggestion: Assign numbers to the tasks
            list.remove(user)
            print(list)
        elif choice == "3":
            print(f"\nTHIS IS YOUR TO-DO-LIST {name}:\n")

            print(list)
            statement = input("\nPress q to quit or c to continue: ")
            if statement == "q":
                break

ToDolist()
