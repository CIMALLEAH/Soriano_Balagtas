global game_library
global user_accounts

game_library = {
 'donkey_kong' :  {'quantity': 3, 'cost' : 2.0},
 'tetris' :  {'quantity': 5, 'cost' : 3.0},
'super_mario' :  {'quantity': 2, 'cost' : 1.0},
}

user_accounts = {'USER1': {'username': 'Soriano', 'password': '12345678', 'balance': 0, 'points': 0, 'game_borrowed': []}}

admin_account = {'admin_username' : 'admin_user', 'admin_password' : 'admin_password'}

def display_available_games():
    pass

def generate_account_id():
    largest_id = 0
    for account_id in user_accounts.keys():
        if account_id.startswith('USER'):
            current_id = int(account_id[4:])  
            largest_id = max(largest_id, current_id)

    return 'USER' + str(largest_id + 1)


def create_user_account():
    global account_id
    account_id = generate_account_id()
    
    set_username = input("please input a username: ")
    set_password = input("please input a password: ")
    if len(set_password) < 8:
        set_password = input("please make the password atleast 8 characters long \n please input a password:")
    else:
        pass
    
    set_balance = 0
    set_points = 0
    game_borrowed_list = [] 
    
    user_accounts[account_id] = {
        'username': set_username,
        'password': set_password,
        'balance': set_balance,
        'points': set_points,
        'game_borrowed': game_borrowed_list,
    }
    print(user_accounts)
    main_page()
    return account_id

    
def log_in():
    username_found = False
    print("Log-in to your account")
    input_username = input("Enter your username: ")

    for key, value in user_accounts.items():
        if value['username'] == input_username:
            username_found = True  
            break
    if username_found:
        input_password = input("Enter your password: ")

    else:
        print("Username not found, please try again")
        log_in()

    if input_password == value['password']:
        password_correct = True
    if username_found and password_correct:
        print("Login successful")
        #search account key
        for key, value in user_accounts.items():
            if value['username'] == input_username:
                account_key = key
        user_account_menu(account_key)
    else:
        print("Incorrect password, please try again")
        log_in()
    
def admin_log_in():
    username_found = False
    print("Log-in to your account")
    input_username = input("Enter your username: ")


    if "admin_user" == input_username:
            username_found = True  
    if username_found:
        input_password = input("Enter your password: ")

    else:
        print("Username not found, please try again")
        log_in()

    if input_password == "admin_password":
        password_correct = True
    if username_found and password_correct:
        print("Admin Login Successful")
        admin_menu()
        
    else:
        print("Incorrect password, please try again")
        admin_log_in()

def admin_menu():
    view_game_library()

def top_up(account_key):
    for key, value in user_accounts.items():
        account_balance = user_accounts[account_id]['balance']

    top_up_amount = int(input("enter the amount you want to top_up: "))

    account_balance += top_up_amount
    
    account_balance[account_id]['balance'] = account_balance

    print(f"you have succesfully deposited {top_up_amount}")
    user_account_menu(account_key)

def user_account_menu(account_key):
    print("=" * 50)
    for key, value in user_accounts.items():
        account_balance = user_accounts[account_key]['balance']
        account_username = user_accounts[account_key]['username']
        account_points= user_accounts[account_key]['points']

    print(f"Hello {account_username}!                     account balance:{account_balance}\n                                    account points:{account_points}")
    print("=" * 50)
    user_account_list(account_key, account_username)
def user_account_list(account_key, account_username):
    print("     1. top up")
    print("     2. rent game")
    print("     3. return a game")
    print("     4. Log-out")

    account_menu_input = input("Enter the number of the option you want to select: ")
    if account_menu_input == "1":
        top_up(account_key)
    elif account_menu_input == "2":
       rent_game_menu()
    elif account_menu_input == "3":
    #    return_game()
       pass
    elif account_menu_input == "4":
        print(f"you have succesfully log-out the account of {account_username}")
        main_page()
    else:
        print("Invalid input, please try again")
        user_account_list(account_key, account_username)

    print("=" * 20)

def rent_game_menu():
    print("please choose a game from our store: ")
    view_game_in_store()
    rent_game()
def view_game_library():
    for game_title, game_details in game_library.items():
            print(f"{game_title}: {game_details['quantity']}, {game_details['cost']}")
            print() 
def view_game_in_store():
    for game_title, game_details in game_library.items():
            if game_details['quantity'] > 0:
                print(f"{game_title}: {game_details['quantity']}, {game_details['cost']}")
            print() 

# {key['game_borrow_list']}")
def rent_game():
    game_select_found = False
    game_search  = input("select which game to borrow")
    for game_title, game_details in game_library.items():
        if game_search == game_title:
            game_select_found = True
            break

        if game_select_found == True:
            print(f"select a method to borrow {game_title}?, with a cost of {game_details['cost']} dollars")
            print("1. via credit")
            print("2. via points")
            print("3. borrow different game")

            rent_input = input("please enter your input:")

            if rent_input == "1":
                pass
            elif rent_input == "2":
                pass
            elif rent_input == "3":
                rent_game_menu()


            # for key, value in user_accounts.items():
            #     borrowed_games = {key['game_borrow_list']}
            #     if game_select in borrowed_games:
            #         print("game is not available")
            #     else:
            #         print(f"you have succesfully borrowed {game_select}")
def main():
        main_page()
    
def main_page(): 
        print("Welcome to GamerShit games and rental store")
        print("=" * 50)       
        print("1. Enter Store/Browse Game Collection")
        #display all games
        print("2. Become a member")
        #create account
        print("3. Log-in")

        print("4. Admin Log-in")

        print("5. Exit store")

        user_input = input("Press corresponding number: ")

        if user_input == '1':  
            view_game_in_store()
            main()
        elif user_input == '2':
            create_user_account()
        elif user_input == '3':
             log_in()
        elif user_input == '4':
            admin_log_in()
        elif user_input == '5':
            exit()
        else: 
            print("please enter a valid input next time")
main()


# tatlo lang muna sa menu at nakakagulo agad, ayusin mo ui and functionality
#create acc, login at forgot password (later na to)
#after ng crreate acc eh ibalik mo sa login
#sabay login auth
#then sa login na ilalagay yung menu ng mga functions para  sa game rental system
# ang gawin mo eh ididisplay ang credentials, currently borrowed game
#game store, display all games, browse games?

#functionalities ng user account nalang





















































# all_books = {}
# book_id = None

# all_borrow = {}
# borrow_id = None

# all_logs = {}
# log_id = None

# def format_dict(dictionary):
#     formatted_dict = "{\n"
#     for key, value in dictionary.items():
#         formatted_dict += f"    '{key}': {value},\n"
#     formatted_dict += "}"
#     return formatted_dict

# def save_dict_to_file(dictionary, file_name):
#     with open(file_name, 'w') as file:
#         formatted_data = format_dict(dictionary)
#         file.write(f"{formatted_data}\n")

# def save_data():
#     save_dict_to_file(all_books, 'all_books.txt')
#     save_dict_to_file(all_borrow, 'all_borrows.txt')
#     save_dict_to_file(all_logs, 'all_logs.txt')

# def load_data_from_file(file_name):
#     data = {}
#     fileHandle = open(file_name, 'r')
#     file_content = fileHandle.read()
#     data = eval(file_content)  
#     fileHandle.close() 

#     return data


# def load_data():
#     global all_books, all_borrow, all_logs
#     all_books = load_data_from_file('all_books.txt')
#     all_borrow = load_data_from_file('all_borrows.txt')
#     all_logs = load_data_from_file('all_logs.txt')

# def restrict_date_month():
#     global date_month
#     while True:
#         user_input_month = input('Enter the order of the month in integer (e.g. January = 1, February = 2, etc.): ')
#         user_input_month = int(user_input_month)
        
#         if 1 <= user_input_month <= 12:
#             if user_input_month == 1:
#                 print('January')
#                 date_month = 'Jan'
#             elif user_input_month == 2:
#                 print('February')
#                 date_month = 'Feb'
#             elif user_input_month == 3:
#                 print('March')
#                 date_month = 'Mar'
#             elif user_input_month == 4:
#                 print('April')
#                 date_month = 'Apr'
#             elif user_input_month == 5:
#                 print('May')
#                 date_month = 'May'
#             elif user_input_month == 6:
#                 print('June')
#                 date_month = 'Jun'
#             elif user_input_month == 7:
#                 print('July')
#                 date_month = 'Jul'
#             elif user_input_month == 8:
#                 print('August')
#                 date_month = 'Aug'
#             elif user_input_month == 9:
#                 print('September')
#                 date_month = 'Sep'
#             elif user_input_month == 10:
#                 print('October')
#                 date_month = 'Oct'
#             elif user_input_month == 11:
#                 print('November')
#                 date_month = 'Nov'
#             else:
#                 print('December')
#                 date_month = 'Dec'
#             break  # Exit the loop after processing valid input
#         else:
#             print('Invalid input. Please enter a number between 1 and 12.')

# def restrict_date_year():
#     global date_year
#     while True:
#         date_year_input = int(input("Year: "))
#         date_year_input =date_year[:4]  # Limit input to first three characters
        
#         if len(date_year_input) == 4 and date_year.isalpha():
#             return date_year == date_year_input
#         elif len(date_year_input) > 3:
#             print("Input was longer than three characters. Only the first three characters will be considered.")
#         else:
#             print("Please enter at least three numbers.")

# def restrict_date_day():
#     global date_day
#     while True:
#         date_day_input = int(input("Day: "))
#         date_day_input = date_day[:2]  # Limit input to first two characters
#         if date_day_input <= 31:
#             if len(date_day_input) == 2 and date_day.isalpha():
#                 return date_day == date_day_input
#             elif len(date_day_input) > 1:
#                 print("Input was longer than one character. Only the first character will be considered.")
#             else:
#                 print("Please enter at least one number.")
#         else: 
#             print("Invalid input. Please enter a number between 1 and 31.")

# def generate_book_id():
#     largest_id = 0
#     for book_id in all_books.keys():
#         if book_id.startswith('B'):
#             current_id = int(book_id[1:])  # Extract numerical part of book_id
#             largest_id = max(largest_id, current_id)

#     return 'B' + str(largest_id + 1)

# def create_book():
#     global book_id
#     book_id = generate_book_id()
    
#     set_title = input("Title of the book: ")
#     set_author = input("Author of the book: ")
#     set_date_published = input('Date Published: ')
#     status = "available"
#     game_borrowed = [] 
    
#     all_books[book_id] = {
#         'title': set_title,
#         'author': set_author,
#         'date_published': set_date_published,
#         'book_status': status,
#         'game_borrowed': game_borrowed,
#         'book_borrowers': None
#     }
#     return book_id


# def create_log(purpose= None):
#     global log_id, person_name  
#     log_id = "L" + str(len(all_logs) + 1)
#     person_name = input("Name: ")

#     print("")
#     print("Date (eg. 1 Jan 2023): ")
#     print("")

#     date_day = (input("Day: "))
#     date_month = (input("Month: "))
#     date_year = (input("Year: "))

#     date = date_day + " " + date_month + " " + date_year

#     print("")
#     print("Time (HH:MM AM/PM):")
#     print("")

#     time_hour = input("Number of hour: ")
#     time_minute = input("Number of minutes: ")
#     time_phrase = input("Choose between AM/PM: ")

#     time = time_hour + ":" + time_minute + " " + time_phrase

#     all_logs[log_id] = {'name' : person_name, 'date' : date, 'time': time, 'purpose': purpose}
#     return log_id, person_name

# def delete_book():
#     global book_id
#     if not all_books:
#         print("Library is empty.")
#         return

#     book_title_find = input('Search for the book title: ')
#     book_author_find = input('Search for the book author: ')
#     found_books = []

#     for book_id, game_details in all_books.items():
#         if 'title' in game_details and 'author' in game_details and game_details['title'] == book_title_find and game_details['author'] == book_author_find:
#             found_books.append((book_id, game_details))

#     if not found_books:
#         print("Book does not exist.")
#         return

#     for book_id, game_details in found_books:
#         print(f"{book_id}: {game_details['title']}, {game_details['author']}, {game_details['date_published']}, {game_details['book_status']}, {(game_details['game_borrowed'])}")
#         print()

#     delete_book_id = input("Enter the book ID of the book you wish to delete: ")

#     if delete_book_id not in all_books:
#         print("Book ID is not valid.")
#         return

#     else: 
#         for delete_book_id, game_details in found_books:
#             if 'book_status' in game_details and game_details['book_status'] == 'unavailable':
#                 print("Book is currently unavailable. Cannot delete.")
#                 return
#             else:

#                 confirm_delete_book = input(f"Please enter 'DELETE' to remove {delete_book_id} or 'CANCEL' to cancel: ")

#                 while confirm_delete_book not in ["DELETE", "CANCEL"]:
#                     confirm_delete_book = input("Invalid input, please enter 'DELETE' or 'CANCEL': ")

#                 if confirm_delete_book == "DELETE":
#                     all_books.pop(delete_book_id, None)
#                     print("Book deleted.")
#                 elif confirm_delete_book == "CANCEL":
#                     print("Deletion canceled.")
#                 else:
#                     print("Invalid input, Make sure its upper case (common sense naman po!).")


                            
     
# def delete_all_books():
#     global all_books
#     remaining_books = {}
#     if all_books == {}: 
#         print("Library is empty.")
#         return
#     for book_id, game_details in all_books.items():
#         if 'book_status' in game_details and game_details['book_status'] == 'unavailable':
#             remaining_books[book_id] = game_details

#     confirm_delete_all_books = input(f'do you wish to delete the entire library?\n please type "DELETE ENTIRE LIBRARY" to proceed: ')
#     if confirm_delete_all_books == "DELETE ENTIRE LIBRARY":
#         all_books.clear()
#         print("Library deleted.")
#     else:
#         print("Invalid input, try again.")
#         return
    
#     all_books = remaining_books.copy()
        
# def view_book():
#     book_title_find = input('Search for the title of the book you wish to view: ')
#     book_title_found = False
    
#     for book_id, game_details in all_books.items():
#         if 'title' in game_details and game_details['title'] == book_title_find:
#             book_title_found = True
            
#             borrowers = game_details['game_borrowed']
#             borrower_names = []
#             for borrow_id in borrowers:
#                 log_number = all_borrow[borrow_id]['log_number']
#                 if log_number in all_logs:
#                     borrower_name = all_logs[log_number]['name']
#                     borrower_names.append(borrower_name)
            
#             # Update the book details with borrower names
#             game_details['game_borrowed'] = borrower_names
            
#             # Print book details with borrower names or indication of no borrowers
#             print(f"Book ID: {book_id}, Book Details: {game_details}")
                
#             break  # Stop the loop once the book is found
    
#     if not book_title_found:
#         print("Book not found.")

# def edit_book():
#     global book_id
#     book_edit_find = input('Search for the book title: ')
#     for book_id, game_details in all_books.items():
#         if 'title' in game_details and game_details['title'] == book_edit_find:
#             book_edit_found = True
#             break
#     if book_edit_found:
#         new_title = input(f"Enter new title for {book_id} :" )
#         new_author = input(f"Enter new author for {book_id} :")
#         new_date_published = input(f"Enter new date published for {book_id} :")

#         all_books[book_id] = {'title': new_title, 'author': new_author, 'date_published': new_date_published, 'book_status': game_details['book_status'], 'game_borrowed': all_books[book_id]['game_borrowed']}
#     else:
#         print("Book not found.")

# def visit_library():
#     global log_id
#     create_log('visit library')

# def view_logbook():
#     for log_id, log_details in all_logs.items():
#         print(f"{log_id}: {log_details['name']}, {log_details['date']}, {log_details['time']}, {log_details['purpose']}")
#         print()



# def view_pending():
#     global book_id
#     for book_id, game_details in all_books.items():
#         if game_details.get('book_status') == 'unavailable':
#             print(f"{book_id}, {game_details}")
# def view_all_transactions():
#     print("input the date of the transaction you wish to view")
#     print("Date (eg. 1 Jan 2023): ")
#     print("In that following format")
#     print("")

#     find_date_day = input("Enter day: ")
#     find_date_month = input("Enter month: ")
#     find_date_year = input("Enter year: ")

#     date_to_search = find_date_day + " " + find_date_month + " " + find_date_year

#     for log_id, log_details in all_logs.items():
#         if log_details.get('date') == date_to_search:  
#             print(f"Log ID: {log_id}, Details: {log_details}")

# def borrow_book():
#     global borrow_id, book_id, log_id
#     create_log('borrow')
#     print("Enter the title and author of the book you wish to borrow:")
#     borrow_title_find = input('Title: ')
#     borrow_author_find = input('Author: ')
#     found_borrow_books = []
    
#     for book_id, game_details in all_books.items():
#         if 'title' in game_details and 'author' in game_details and game_details['title'] == borrow_title_find and game_details['author'] == borrow_author_find:
#             found_borrow_books.append((book_id, game_details))

#     if not found_borrow_books:
#         print("Book does not exist.")
#         return
    
#     print("book found")
#     for book_id, game_details in found_borrow_books:
#         print(f"{book_id}: {game_details['title']}, {game_details['author']}, {game_details['date_published']}, {game_details['book_status']}, {(game_details['game_borrowed'])}")
#         print()
#     borrow_book_id = input("Enter the book ID of the book you wish to borrow: ")

#     if borrow_book_id not in all_books:
#         print("Book ID is not valid.")
#         return

#     else:
#         for borrow_book_id, game_details in found_borrow_books:
#             if 'book_status' in game_details and game_details['book_status'] == 'unavailable':
#                 print("Book is currently unavailable. Cannot borrow.")
#                 return
#             else:
#                 borrow_id = 'BL' + str(len(all_borrow) + 1)
#                 print("Enter the date of return: (e.g., 1 Jan 2023)")
#                 return_date_day = input("Day: ")
#                 return_date_month = input("Month: ")
#                 return_date_year = input("Year: ")
#                 return_date = return_date_day + " " + return_date_month + " " + return_date_year

#                 new_book_status = 'unavailable'

#                 # Append the new borrow ID to the list of borrowers for the specific book
#                 all_books[borrow_book_id]['game_borrowed'].append(borrow_id)

#                 all_borrow[borrow_id] = {'book_number': borrow_book_id, 'log_number': log_id, 'date_of_return': return_date}

#                 all_books[borrow_book_id] = {
#                     'title': game_details['title'],
#                     'author': game_details['author'],
#                     'date_published': game_details['date_published'],
#                     'book_status': new_book_status,
#                     'game_borrowed': all_books[borrow_book_id]['game_borrowed']  # Updated game_borrowed
#                 }
#                 return borrow_id 

# def return_book():
#     global borrow_id, book_id, log_id
#     create_log('return')
#     print("enter the title and author of the book you wish to return")
#     return_title_find = input('title: ')
#     return_author_find = input('author: ')

#     for book_id, game_details in all_books.items():
#         if 'title' in game_details and 'author' in game_details and game_details['title'] == return_title_find and game_details['author'] == return_author_find:
#             book_return_found = True
#             break
#     if book_return_found:
#         for borrow_id, borrow_details in all_borrow.items():
#             if borrow_details.get('book_number') == book_id:
#                 for log_id, log_details in all_logs.items():
#                     if person_name == log_details.get('name'):
#                         return_book_status = 'available'
#                         all_books[book_id] = {'title': game_details['title'], 'author': game_details['author'], 'date_published': game_details['date_published'], 'book_status': return_book_status, 'game_borrowed': all_books[book_id]['game_borrowed']}
#                 break
#     else:
#         print("Book not found.")

# def view_all_entries(borrow_id):
#     for borrow_id, borrow_info in all_borrow.items():
#         book_number = borrow_info['book_number']
#         log_number = borrow_info['log_number']
#         date_of_return = borrow_info['date_of_return']
        
#         book_info = all_books.get(book_number)
#         log_info = all_logs.get(log_number)
        
#         if book_info and log_info:
#             title = book_info['title']
#             author = book_info['author']
#             date_published = book_info['date_published']
#             borrower = all_logs[log_number]['name']
            
#             print(f"{borrow_id}: {{'Title': '{title}', 'Author': '{author}', 'Date Published': '{date_published}', 'Date Return': '{date_of_return}', 'Borrower': '{borrower}'}}")
#             print()

# def view_expected_returns(borrow_id):
#     print("Input the date of the transaction you wish to view")
#     print("Date (e.g., 1 Jan 2023): ")
#     print("In that following format")
#     print("")

#     expected_date_day = input("Enter day: ")
#     expected_date_month = input("Enter month: ")
#     expected_date_year = input("Enter year: ")

#     expected_date_to_search = expected_date_day + " " + expected_date_month + " " + expected_date_year

#     found = False

#     for borrow_id, borrow_info in all_borrow.items():
#         if borrow_info.get('date_of_return') == expected_date_to_search:
#             found = True
#             book_number = borrow_info['book_number']
#             log_number = borrow_info['log_number']
            
#             book_info = all_books.get(book_number)
#             log_info = all_logs.get(log_number)
            
#             if book_info and log_info:
#                 title = book_info['title']
#                 author = book_info['author']
#                 date_published = book_info['date_published']
#                 book_status = book_info['book_status']
#                 borrower = all_logs[log_number]['name']
                
#                 print(f"{borrow_id}: {{'Title': '{title}', 'Author': '{author}', 'Date Published': '{date_published}', 'status': '{book_status}', 'Borrower': '{borrower}'}}")
#                 print()

#     if not found:
#         print("There are no expected returns on that date.")

# def print_books():
#     for book_id, game_details in all_books.items():
#         print(f"{book_id}: {game_details['title']}, {game_details['author']}, {game_details['date_published']}, {game_details['book_status']}, {(game_details['game_borrowed'])}")
#         print() 



# def borrow_section():
#     user_input = None
#     while user_input != '5':
#         print("1. Borrow book")
#         print("2. Return book")
#         print("3. View all entries")
#         print("4. View expected returns")
#         print("5. back to main menu")

#         user_input = input("Press corresponding number: ")
        
#         if user_input == '1':
#             borrow_book()
#         elif user_input == '2':
#             return_book()
#         elif user_input == '3':
#             view_all_entries(borrow_id)
#         elif user_input == '4':
#             view_expected_returns(borrow_id)
#         elif user_input == '5':
#             main_page()
# def book_section():
#     user_input = None
#     while user_input != '9':
#         print("1. Create book")
#         print("2. Print all books")
#         print("3. Delete book")
#         print("4. Search and view for a book")
#         print("5. Delete all library: ")
#         print("6. View book")
#         print("7. Edit book")
#         print("8. View pending books")
#         print("9. back to main menu")

#         user_input = input("Press corresponding number: ")

#         if user_input == '1':
#             create_book()
#         elif user_input == '2':
#             print_books()
#         elif user_input == '3':
#             delete_book()
#             pass
#         elif user_input == '4':
#             view_book()
#         elif user_input == '5':
#             delete_all_books()
#         elif user_input == '6':
#             view_book()
#         elif user_input == '7':
#             edit_book()
#         elif user_input == '8':
#             view_pending()
#         elif user_input == '9':
#             main_page()
#         else:
#             print("Invalid input.")

# def log_section():
#     user_input = None
#     while user_input != '5':
#         print("1. Visit Library")
#         print("2. View Pending")
#         print("3. View all transactions")
#         print("4. Back to main menu")

#         user_input = input("Press corresponding number: ")

#         if user_input == '1':  
#             visit_library()
#         elif user_input == '2':
#             view_logbook()
#         elif user_input == '3':
#             view_all_transactions()
#         elif user_input == '4':
#             main_page()
#         else:
#             print("Invalid input.")

# def main():
#         main_page()
# def main_page():        
#         print("1. Book Section")
#         print("2. Log Section")
#         print("3. Borrow Section")
#         print("4. Save/create database")
#         print("5. Load data")
#         print("6. Exit command")

#         user_input = input("Press corresponding number: ")

#         if user_input == '1':  
#             book_section()
#         elif user_input == '2':
#             log_section()
#         elif user_input == '3':
#              borrow_section()
#         elif user_input == '4':
#             save_data()
#             print("Data saved\succesfully created a file.")
#             main_page()
#         elif user_input == '5':
#             load_data()
#             main_page()
#         elif user_input == '6':
#             exit()
#         else:
#             print("Invalid input.")

# main()
