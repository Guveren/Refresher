#Lets refresh, a simple todo list python program 
#To run on terminal type "python3 todolist.py"
action_items = []

#function to the add the tasks 

def add(task):
    action_items.append(task)
    print(f"Task '{task}' was added to the to-do list!")

def remove(index):
    if 1 <= index <= len(action_items):
        removeditems = action_items.pop(index - 1)
        print(f"The action item '{removeditems}' was removed from the to-do list")
    else:
        print("Invalid action item!")


def displaylist():
    if not action_items:
        print("there are no action items present in the to-do list")
    else:
        print("Your to-do list\n")
        for index, action_item in enumerate(action_items, start=1):
            print (f"{index}. {action_item}")
#main 
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    selection =  input("Enter your choice: ")

    if selection == "1":
        displaylist()
    elif selection == "2":
        task = input("Enter the action item: ")
        add(task)
    elif selection == "3":
        displaylist()
        task_index = int(input("Enter the task number to remove: "))
        remove(task_index)
    elif selection == "4":
        print("End of program!")
        break
    else:
        print("Invalid selection. Please try again.")

