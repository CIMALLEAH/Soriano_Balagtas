global game_library
global user_accounts

game_library = {
 'donkey_kong' :  {'quantity': 3, 'cost' : 2.0},
 'tetris' :  {'quantity': 5, 'cost' : 3.0},
'super_mario' :  {'quantity': 2, 'cost' : 1.0},
}

user_accounts = {}

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
        set_password = input("please make the password atleast 8 characters long")
    else:
        pass    
    set_balance = 0
    set_points = 0
    set_status = "available"
    game_borrowed_list = [] 
    
    user_accounts[account_id] = {
        'username': set_username,
        'password': set_password,
        'balance': set_balance,
        'points': set_points,
        'status': set_status,
        'game_borrowed': game_borrowed_list,
    }
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
        
    else:
        print("Incorrect password, please try again")
        admin_log_in()

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

    print(f"Hello {account_username}!                     account balance:{account_balance}")
    print(account_key)
    print("=" * 50)
   
    print("     1. top up")
    print("     2. rent game")
    print("     3. return a game")
    print("     4. Log-out")

    account_menu_input = input("Enter the number of the option you want to select: ")
    if account_menu_input == "1":
        top_up(account_key)
    elif account_menu_input == "2":
       rent_game()
    elif account_menu_input == "3":
    #    return_game()
       pass
    elif account_menu_input == "4":
       main_page()
    else:
        print("Invalid input, please try again")
    print("=" * 20)

def rent_game():
        
    print("1. View Game Library")
    print("2. borrow a game" )
    print("4. Return Game")
    print("5. Exit command")

    user_input = input("Press corresponding number: ")

    if user_input == '1':  
        view_game_library()
    elif user_input == '2':
        rent_game_main()
    elif user_input == '3':
        # return_game()
        pass
    elif user_input == '4':
        exit()
    else: 
        print("please enter a valid input next time")

def view_game_library():
    for game_title, game_details in game_library.items():
        for key, value in user_accounts.items():
            print(f"{game_title}: {game_details['quantity']}, {game_details['cost']}, {game_details['date_published']}, {key['game_borrow_list']}")
            print() 

def rent_game_main():
    view_game_library()
    game_select_found = False
    game_select = input("select which game to borrow")
    for game_title, game_details in game_library.items():
        if game_select == game_title:
            game_select_found = True
        
        if game_select_found == True:
            for key, value in user_accounts.items():
                borrowed_games = {key['game_borrow_list']}
                if game_select in borrowed_games:
                    print("game is not available")
                else:
                    print(f"you have succesfully borrowed {game_select}")
                


def main():
        main_page()
    
def main_page():        
        print("1. Display Available Games")
        print("2. Register User")
        print("3. Log-in")
        print("4. Admin Log-in")
        print("5. Exit command")

        user_input = input("Press corresponding number: ")

        if user_input == '1':  
            pass
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
