# Library Mangager

books = []
title_book = []
author = []
available = []
year = []
quantity = []

user_name = input("Please Enter you username: ")

def show_menu():
    print("\n Welcome to", user_name, "\n")
    print("1. Add book")
    print("2. Search book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Show all books")
    print("6. Remove book")
    print("7. Exit")

def add_book():
    add_new_book = input("Please enter name book: ")
    add_qua_book = int(input("Please enter quantity book: "))
    insert_author_book = input("Please enter author: ")
    insert_availble_book = input("Abailble or Not availble: ")
    insert_year_book = int(input("Enter year create: "))
            
    books.append(add_new_book)
    quantity.append(add_qua_book)
    author.append(insert_author_book)
    available.append(insert_availble_book)
    year.append(insert_year_book)
    return

def search_book():
    search_book_new = input("Enter Value: ")

    if search_book_new in books:
        find_book = books.index(search_book_new)
        find_n_quantity = quantity[find_book]
        find_n_year = year[find_book]
        find_n_available = available[find_book]
        find_n_author = author[find_book]
        print(search_book_new)
        print("----")
        print(find_n_author, '|', find_n_quantity, '|', find_n_year, '|', find_n_available)
    else:
        print("Not Difound")

def borrow_book():
    name_book_borrow = input("Enter name book: ")
    refind = name_book_borrow in books
    if refind:
        u_enter_quantity = int(input("Enter quontity: "))
        v_books_value = books.index(name_book_borrow)
        new_quantity = quantity[v_books_value] - u_enter_quantity
        app_new_qua = quantity.insert(v_books_value, new_quantity)
        print(new_quantity)
        return new_quantity
    else:
        print("The operation failed")


def return_book():
    while True:
        insert_new_book = input("please enter new book, Enter '0' Exit: ")

        if True and insert_new_book == "0":
            break
        else:
            insert_quantity_book = int(input("Please enter you quantity: "))
            insert_author_book = input("Please enter author: ")
            insert_availble_book = input("Abailble or Not availble: ")
            insert_year_book = int(input("Enter year create: "))

            books.append(insert_new_book)
            quantity.append(insert_quantity_book)
            author.append(insert_author_book)
            available.append(insert_availble_book)
            year.append(insert_year_book)
            
            print("Done")

def show_all_books():
    for show in books:
        show_all = books.index(show)
        print("\n----")
        print(show)
        print(quantity[show_all], '|', author[show_all], '|', year[show_all], '|', available[show_all])

def remove_book():
    print("All books")
    print("========")
    print(books)
    print("========")
    assimint_book = input("Please enter item remove: ")

    if assimint_book in books:
        u_qua_inx = books.index(assimint_book)
        remove_q = quantity[u_qua_inx]
        remove_a = author[u_qua_inx]
        remove_y = year[u_qua_inx]
        remove_av = available[u_qua_inx]

        books.remove(assimint_book)
        quantity.remove(remove_q)
        author.remove(remove_a)
        year.remove(remove_y)
        available.remove(remove_av)

        print("Done", assimint_book)
    else:
        print("Not difund")

def main():
    while True:
        show_menu()

        choose_menu = input("Please Choose Item: ")
        if choose_menu == "1":
            add_book()
        elif choose_menu == "2":
            search_book()
        elif choose_menu == "3":
            borrow_book()
        elif choose_menu == "4":
            return_book()
        elif choose_menu == "5":
            show_all_books()
        elif choose_menu == "6":
            remove_book()
        else:
            # print("Exit, Thank you", user_name)
            break

# main()