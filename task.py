todo=list()
def task():
    addtask=int(input("want to add task ? \n press 1 to enter the task \n press 2 to mark as complete and remove \n press 3 to view the to do list \n enter 4 to exit:"))
    while addtask!=4:
        if(addtask==1):
            task=input("enter the task:")
            todo.append(task)
            print("task added successfully")
        if(addtask==2):
            if(len(todo)==0):
                print("Invalid Choice:list does not contain any item")
            else:
                print(todo)
                index=input("enter the task to remove from above list:")
                if index not in todo:
                    print("item does not exists select the correct option")
                else:
                    todo.remove(index)
                    print("Task removed")
        if addtask==3:
            if len(todo)!=0:
                print("To Do List")
                for t in todo:
                 print(t)
            else:
                print("TO do list is empty")
        addtask=int(input("\nenter choice again: "))
        
task()


