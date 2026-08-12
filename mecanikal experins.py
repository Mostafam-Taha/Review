balance = 0.0
# اضافة المال > اضافة مكان الانفاق > اضافة الساعة التي تم الانفاق فيها > اضافة اي ملاحظات.
list_data_name_tr = ["Food", "To RAM space", "ATM withdrawal", "From RAM space", "IPN transfer", "To Home space", "moaaz.syn"]
list_data_many_tr = [55, 12.70, 273, 50, 155, 118, 10]
list_data_date_tr = ["04:20 PM", "12:13 PM", "12:12 PM", "09:49 PM", "09:47 PM", "08:45 PM", "11:03 AM"]


def login_user():
    print("Login User")
    log_nukname = input("Enter is numname: ")
    log_username = input("Enter is username: ")
    log_password = input("Enter is passwrod: ")

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
    else:
        print(f"Failed: {many_transfering} EGP")

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


def show_balance():
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
    print(item_list)

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
            print("Thank you!")
            break
main()