import os
import csv
from datetime import datetime

name_files = "data_todo_list.csv"
data = []
def show_menu():
    print("\n==== Welcome To User ====")
    print("1. Add To Task")
    print("2. Show All Tasks")
    print("0. Exit")

def load_tasks():
    global data
    if os.path.isfile(name_files):
        with open(name_files, "r", newline="") as f:
            reader = csv.DictReader(f)
            data = list(reader)

def file_save():
    file_exists = os.path.isfile(name_files)
    with open(name_files, "a", newline="") as create_file:
        x = ["name", "created_at", "done"]
        writer = csv.DictWriter(create_file, x)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data[-1])

def add_to_task():
    add_input_task = input("Please Enter is new task: ")

    created_at = datetime.now().strftime("%Y-%B-%d %H:%M:%S")
    new_task = {
        "name": add_input_task,
        "created_at": created_at,
        "done": True
    }
    data.append(new_task)
    file_save()


def show_all_tasks():
    with open(name_files, "r") as show_file_reading:
        reader = csv.DictReader(show_file_reading)
        for row in reader:
            print (f"{row["name"]} | {row["created_at"]} | {row["done"]}")

def main():
    load_tasks()
    while True:
        show_menu()

        try:
            user_input_choose = int(input("\nEnter You number: "))
        except:
            print("Chatacter not number")
            continue
        if user_input_choose == 1:
            add_to_task()
        elif user_input_choose == 2:
            show_all_tasks()
        else:
            print("Thank You!")
            break
main()
