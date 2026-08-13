balance = 0.0
number_of_attemy = 5
attemy = 0

user_login = {
    "username": "mostafamohamedtaha",
    "nukname": "mostafamtaha",
    "password": 12341234
}
# Virtual data
# list_data_name_tr = ["Food", "To RAM space", "ATM withdrawal", "From RAM space", "IPN transfer", "To Home space", "moaaz.syn"]
# list_data_many_tr = [55, 12.70, 273, 50, 155, 118, 10]
# list_data_date_tr = ["04:20 PM", "12:13 PM", "12:12 PM", "09:49 PM", "09:47 PM", "08:45 PM", "11:03 AM"]

list_data_name_tr = []
list_data_many_tr = []
list_data_date_tr = []

def show_dashboard():
    print("\n1. Show Balance")
    print("2. Add Balance")
    print("3. Updata new balance")
    print("0. Exit")

def add_balance():
    global balance

    name_transfering = input("Please Enter you name transfer: ")
    many_transfering = float(input("Please Enter you many: "))
    date_transfering = input("Please enter is you date: ")

    if many_transfering > 0:
        list_data_name_tr.append(name_transfering)
        list_data_many_tr.append(many_transfering)
        list_data_date_tr.append(date_transfering)
            
        # Show user experins
        show_user_experins_index = list_data_name_tr.index(name_transfering)
        show_user_experins_dic = list_data_name_tr[show_user_experins_index]

        show_user_experins_index_many = list_data_many_tr.index(many_transfering)
        show_user_experins_dic_many = list_data_many_tr[show_user_experins_index_many]

        show_user_experins_index_date = list_data_date_tr.index(date_transfering)
        show_user_experins_dic_date = list_data_date_tr[show_user_experins_index_date]

        balance += many_transfering

        print("Transactions")
        print("----")
        print(f"{show_user_experins_dic}\n{show_user_experins_dic_many} EGP\n{show_user_experins_dic_date}")
    else:
        print(f"Failed: {many_transfering} EGP")

def show_balance():
    global balance
        
    print(f"==== {balance} EGP ====\n")
    len_val =len(list_data_name_tr)
    for value_li in range(len_val):
        print(f"{list_data_name_tr[value_li]}: {list_data_many_tr[value_li]} EGP, {list_data_date_tr[value_li]}")

def update_new_balance():
    len_print_key = len(list_data_name_tr) 
    for key_main_num in range(len_print_key): 
        print(f"\n{key_main_num + 1}. {list_data_name_tr[key_main_num]}: {list_data_many_tr[key_main_num]} EGP{list_data_date_tr[key_main_num]}\n")

    choose = input("Please Enter is item is value: ")
    item_list = choose in list_data_name_tr
    
    if item_list:
        index_value = list_data_name_tr.index(choose)

        update_in_name = input("Please enter is new name: ")
        update_in_balance = float(input("Please enter is new balance: "))
        update_in_date = input("Please enter is new name: ")
        search_value_list_one = list_data_name_tr[index_value] = update_in_name
        search_value_list_two = list_data_many_tr[index_value] = update_in_balance
        search_value_list_three = list_data_date_tr[index_value] = update_in_date
        print(f"Done, transfer form {choose} => {list_data_name_tr[index_value]}")
    else:
        print(f"Not defound {choose}!")

def main():
    while True:
        show_dashboard()

        ti_user = input("Please enter you show dashboard: ")
        
        if ti_user == "1":
            show_balance()
        elif ti_user == "2":
            add_balance()
        elif ti_user == "3":
            update_new_balance()
        else:
            print(f"Thank you {user_login.get("nukname")}!")
            break

def login_user(fun_value_password):
    global attemy
    print("====Login User====")

    while attemy != number_of_attemy:
        log_password = int(input("Please Enter is password correct: "))

        if len(str(log_password)) != 8:
            print("Ammm, Sorry 8 degits")
            continue

        if log_password == fun_value_password:
            print("correct")
            main()
            break
        else:
            attemy = attemy + 1
            print("Incorrect")

        if attemy != number_of_attemy:
            print(f"UP {attemy} from 5")
        else:
            print("Stop Program")

login_user(user_login.get("password"))
