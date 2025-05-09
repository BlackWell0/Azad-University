import json

task_menu = [" 1 - new task",
             " 2 - Show all tasks",
             " 3 - Remove all tasks",
             " 4 - Remove  one task between all tasks",
             " 5 - Mark these as done.",
             " 6 - Save and exit"]

task_list = []
ok_list = [1, 2, 3, 4, 5, 6]

task_list = []

try:
    f = open("tasks.txt", "r", encoding="utf-8")
    for line in f:
        parts = line.strip().split("|")
        if len(parts) == 2:
            title = parts[0]
            condition = parts[1] == "1"
            task_list.append({"Task's title ": title, "condition": condition})
    f.close()
except:
    pass


while True:
    print("\n".join(task_menu))
    task = int(input("Please enter the numbers of one of the available tasks. : "))

    match task:
        case 1:
            print("You have entered the tasks menu ")
            new_task = input("Enter your task: ")
            task_list.append({"Task's title ": new_task, "condition": False})
            print("Last value : ")
            print(task_list[-1])

        case 2:
            print("All tasks :  ")
            print(task_list)

        case 3:
            print("All tasks are deleted")
            task_list[0:] = []

        case 4:
            print("Select the task to remove")
            count = 1
            for index in task_list:
                print(f"Your task is {index} and its number {count}")
                count += 1
            remove_task = int(input("Enter the number of the task: "))
            let = remove_task - 1
            x = len(task_list)
            if 0 <= let < x:
                del task_list[let]
                print("Your task is removed")
            else:
                print("Please enter a valid task number")

        case 5:
            print("You have entered the 'Mark as done' menu.")
            count = 0
            for i in task_list:
                keys = list(i.keys())
                second_key = keys[1]
                count += 1
                print(f"Task {count} and Condition {i[second_key]}")
            x = int(input("task mark : "))
            index = x - 1
            if 0 <= index < len(task_list):
                task_list[index]["condition"] = not task_list[index]["condition"]

        case 6:
            print("You have entered the 'Save and exit' menu.")
            with open("tasks.txt", "w", encoding="utf-8") as f:
                for task in task_list:
                    title = task["Task's title "]
                    condition = "1" if task["condition"] else "0"
                    f.write(f"{title}|{condition}\n")
            break

        case _:
            print("You entered the wrong number. Please enter one of the numbers in the list. !")
            print("Run this program again")
