from datetime import datetime as Date
from os import system
from time import sleep
from getpass import getpass
import random
import session
import database
import validation


# Initializing the system
def init():
    system('clear')
    print('')
    print('Welcome to the ATM!')
    print('Today is ' + Date.now().strftime("%B %d, %Y (%H:%M:%S)"))
    print('')
    # Checking for existing account
    have_account = int(input('Do you have account with us?\n 1. Yes\n 2. No\n: '))
    print('')
    if have_account == 1 :
        login()
    elif have_account == 2:
        register()
    else:
        print('\nYou have selected invalid option')
        # Returns to previous selection
        init()


#Login an existing user
def login():
    user_tries = 3
    while user_tries > 0:
        system('clear')
        print('****** LOGIN ******')
        # User inputs known account number
        # TODO add choice to login via email

        account_number_from_user = input('What is your account number?\n: ')
        password = getpass('What is your Password?\n: ')

        is_valid_account_number = validation.account_number_validation(account_number_from_user)
        if is_valid_account_number:
            user_account_number = int(account_number_from_user)
            # Checking Database for given account number
            account = database.authenticated_user(user_account_number, password)
            if account:
                break
            else:
                print('Invalid account or password, please try again')
                sleep(2)
                user_tries -= 1

        else:
            print('Invalid account or password, please try again')
            sleep(2)
            user_tries -= 1
    else:
        system('clear')
        print('Number of tries exceeded, GoodBye')
        sleep(2)
        quit()
    session.start_session(account)
    bank_operation(account)


# Register a new user
def register():
    system('clear')
    print('****** REGISTER ******')
    email = input('What is your email address?\n: ')
    is_valid_email = validation.email_validation(email)
    if not is_valid_email:
        print("Invalid Email address: (" + email + "), Please try again.")
        sleep(1)
        register()
    first_name = input('What is your First name?\n: ')
    last_name = input('What is your Last name?\n: ')

    password = getpass('Create a password for yourself.\n: ')
    confirm_pass = getpass('Re-enter your Password.\n: ')
    # do password match
    if password != confirm_pass:
        print('Passwords do not match, Please try again.')
        sleep(2)
        register()
    try:
        account_number = generate_account_number()
    except ValueError:
        print("Account number generation failed, returning to Main Menu")
        init()
    sleep(1)
    user_details = {
        'account_number': account_number,
        'first_name': first_name,
        'last_name': last_name,
        'email': email.lower(),
        'password': password,
        'balance': 0,
    }
    is_user_created = database.create(account_number, user_details)
    if is_user_created:
        system('clear')
        print('Your Account has been created')
        print(' === === === === === === ')
        print('Your Account number is: %d' % account_number)
        print('Make sure you keep it safe.')
        print(' === === === === === === ')
        input('Taking you to Login, Press Enter/Return to continue.')
        # TODO have auto-login after register
        login()
    else:
        print("Registration failed, Something went wrong")
        print("Returning to Account Creation")
        sleep(2)
        register()


def bank_operation(account):
    system('clear')
    print('Welcome back %s %s!' % (account['first_name'], account['last_name']))
    print('''These are the available options:
  1. Get Current Balance
  2. Cash Deposit
  3. Withdrawal
  4. Change User Details --- Not yet available
  5. Report a Complaint
  6. Logout
  7. Exit''')

    selected_option = int(input("Please select an option: \n"))
    if selected_option == 1:
        get_balance(account)
    elif selected_option == 2:
        deposit_operation(account)
    elif selected_option == 3:
        withdrawal_operation(account)
    elif selected_option == 4:
        print('Changing User Details not yet available')  # TODO - implement
        # change_user_details(account)
        sleep(1)
        bank_operation(account)
    elif selected_option == 5:
        report_complaint(account)
    elif selected_option == 6:
        logout(account)
    elif selected_option == 7:
        print('You selected Exit')
        session.end_session(account)
        print('Closing application')
        sleep(1)
        exit()
    else:
        print('Invalid option selected')
        bank_operation(account)


def get_balance(account):
    system('clear')
    print('Your Current Balance is %d' % account['balance'])
    print('''These are the available options:
  1. Cash Deposit
  2. Withdrawal
  3. Return to Previous Menu''')
    selected_option = int(input("Please select an option: \n"))
    if selected_option == 1:
        deposit_operation(account)
    elif selected_option == 2:
        withdrawal_operation(account)
    elif selected_option == 3:
        print('Returning to previous menu.')
        sleep(2)
        bank_operation(account)
    else:
        print('Invalid option selected')
        sleep(1)
        get_balance(account)


def deposit_operation(account):
    system('clear')
    print('You selected Cash Deposit')
    print('-' * 20)
    print('Your Current Balance is %d' % account['balance'])
    deposit_amount = int(input('How much would you like to Deposit?\n: '))
    account['balance'] += deposit_amount
    print('-' * 20)
    print('Depositing %d into account' % deposit_amount)
    print('New Balance : %d' % account['balance'])
    print('Returning to previous menu.')
    sleep(3)
    database.update(account)
    bank_operation(account)


def withdrawal_operation(account):
    system('clear')
    print('You selected Withdrawal')
    print('-' * 20)
    print('Your Current Balance is %d' % account['balance'])
    withdrawal_amount = int(input('How much would you like to withdraw?\n: '))
    if withdrawal_amount > account['balance']:
        print('-' * 20)
        print('Amount exceeds Current Balance, returning to previous menu.')
    else:
        system('clear')
        account['balance'] -= withdrawal_amount
        print('-' * 20)
        print('Amount withdrawn from account: %d' % withdrawal_amount)
        print('New Balance : %d' % account['balance'])
        print('Returning to previous menu.')
    sleep(3)
    database.update(account)
    bank_operation(account)

def change_user_details(account):
    # List user details
    print('User Details:')
    for k, v in account.items():
        if k == 'password':
            continue
        print(f'{k.capitalize()} : {v}')
    # TODO
    # Offer User option to change details
    # Option what to change
    # Update user_details with: database.update(account)


def report_complaint(account):
    system('clear')
    print('You selected Report a Complaint')
    print('-' * 20)
    complaint = input('Please state your complaint. \n: ')
    print('Thank you for your input.')
    print('Submitting complaint..')
    account['complaint'] = complaint
    sleep(2)
    print('Returning to previous menu.')
    sleep(2)
    database.update(account)
    bank_operation(account)


def logout(account):
    system('clear')
    session.end_session(account)
    print('Returning to Login screen')
    init()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


init()
# change_user_details({'account_number': 1, 'first_name': 'System', 'last_name': 'Admin', 'password': 'SystemAdmin', 'email': 'admin@system.com', 'balance': 0})