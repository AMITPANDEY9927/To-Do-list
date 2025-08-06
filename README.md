# To-Do-list

This is a command-line based To-Do List application written in Python. It allows the user to manage daily tasks through a simple menu-driven interface.

## Features

- Add a task to the list
- Mark a task as complete (remove it)
- View all tasks in the list
- Exit the application

## How It Works

The script repeatedly prompts the user with the following options:

1. **Add a task**  
   User inputs the task, and it is added to the `todo` list.

2. **Remove a completed task**  
   Displays the current list and allows the user to input the task name to remove. If the task doesn't exist, it shows an appropriate message.

3. **View tasks**  
   Prints all tasks currently in the `todo` list.

4. **Exit**  
   Ends the program.

## Sample Run

want to add task ? 
 press 1 to enter the task 
 press 2 to mark as complete and remove 
 press 3 to view the to do list 
 enter 4 to exit:1
enter the task:reading
task added successfully

enter choice again: 1
enter the task:market
task added successfully

enter choice again: 1
enter the task:repair
task added successfully

enter choice again: 3
To Do List
enter the task:market
task added successfully

enter choice again: 1
enter the task:repair
task added successfully

enter choice again: 3
To Do List
reading
market
repair

enter choice again: 2
['reading', 'market', 'repair']
enter the task to remove from above list:repair
Task removed

enter choice again: 3
To Do List
reading
market

enter choice again: 4
