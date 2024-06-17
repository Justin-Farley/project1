import os
current_list = []
status = []
def clear_console():
    os.system("clear")

def showmenu():
    print("Welcome to the To-Do list App!")
    print("""
Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
         """)


def showtasks():
    if len(current_list) == 0:
        print("There are 0 tasks")
    else:
        print('Current Tasks:')
        for i in range(len(current_list)):
            print(f"task: {current_list[i]}")
            print(f"status: {status[i]}")
            print("-----------")
            
def addtask():
    add = input("add a task. ")
    current_list.append(add)
    status.append("incomplete")
    print("task added!")


def completetask():
    completed = input("which task do you want to complete ")
    x = current_list.index(completed)
    status[x] = "completed"

def deletetask():
    delete = input("which task would you like to delete? ")
    current_list.remove(delete)
    print("task has be deleted")


    

while True:
    showmenu()
    user = input("Please select a number 1-5. ")   
    if user == '1':
        addtask()
        
    elif user == '2':
        showtasks()
    elif user == '3':
        completetask()
    elif user == '4':
        deletetask()
    elif user == '5':
        break

    
    




    



    
