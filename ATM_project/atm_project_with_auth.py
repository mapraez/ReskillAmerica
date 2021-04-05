from datetime import datetime as Date
from os import system
from time import sleep
import random
from database import *

# Initializing the system
def init():
    system('clear')
    print('')
    print('Welcome to the ATM!')
    print('Today is ' + Date.now().strftime("%B %d, %Y (%H:%M:%S)"))
    print('')
    # Checking for existing account
    haveAccount = int(input('Do you have account with us?\n 1. Yes\n 2. No\n: '))
    print('')
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('\nYou have selected invalid option')
        # Returns to previous selection
        init()

#Login an existing user
def login():
    userTries = 3
    while(userTries > 0):
        system('clear')
        print('****** LOGIN ******')
        # User inputs known account number
        ## TODO add choise to login via email
        accountNumberFromUser = int(input('What is your account number?\n: '))
        password = input('What is your Password?\n: ')
        # Checking Database for given account number
        if accountNumberFromUser in knownAccounts.keys():
            if password == knownAccounts[accountNumberFromUser]['password']:
                break
            else:
                print('Invalid account or password, please try again')
                userTries -= 1
        else:
            print('Invalid account or password, please try again')
            userTries -= 1
    else:
        system('clear')
        print('Number of tries exceeded, GoodBye')
        quit()
    account = knownAccounts[accountNumberFromUser]
    bankOperation(account)



# Register a new user
def register():
    system('clear')
    print('****** REGISTER ******')
    ## TODO add regex to verify legit email address
    email = input('What is your email address?\n: ')
    first_name = input('What is your First name?\n: ')
    last_name = input('What is your Last name?\n: ')
    password = input('Create a password for yourself.\n: ')
    accountNumber = generateAccountNumber()
    print('Creating account')
    knownAccounts[accountNumber] = {
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
        'password' : password,
        'balance' : 0, 
    }
    system('clear')
    print('Your Account has been created')
    print(' === === === === === === ')
    print('Your Account number is: %d' % accountNumber)
    print('Make sure you keep it safe.')
    print(' === === === === === === ')
    input('Taking you to Login, Press Enter/Return to continue.')
    

    login()

def bankOperation(account):
    system('clear')
    print('Welcome back %s %s!' % (account['first_name'], account['last_name']))
    print('These are the available options:')
    print('1. Cash Deposit')
    print('2. Withdrawal')
    print('3. Report a Complaint')
    print('4. Logout')
    print('5. Exit')
    
    selectedOption = int(input("Please select an option: \n"))

    if(selectedOption == 1):
        depositOperation(account)
    elif(selectedOption == 2):
        withdrawlOperation(account)
    elif(selectedOption == 3):
        reportComplaint(account)
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        print('You selected Exit')
        print('Closing application')
        sleep(1)
        exit()
    else:
        print('Invalid option selected')
        bankOperation(account)

def depositOperation(account):
    system('clear')
    print('You selected Cash Deposit')
    print('-' * 20)
    print('Your Current Balance is %d' % account['balance'])
    depositAmount = int(input('How much would you like to Deposit?\n: '))
    account['balance'] += depositAmount
    print('-' * 20)
    print('Depositing %d into account' % depositAmount)
    print('New Balance : %d' % account['balance'])
    print('Returning to previous menu.')
    sleep(3)
    bankOperation(account)

def withdrawlOperation(account):
    system('clear')
    print('You selected Withdrawal')
    print('-' * 20)
    print('Your Current Balance is %d' % account['balance'])
    withdrawalAmount = int(input('How much would you like to withdraw?\n: '))
    if(withdrawalAmount > account['balance']):
        print('-' * 20)
        print('Amount exceeds Current Balance, returning to previous menu.')
        sleep(3)
    else:
        system('clear')
        account['balance'] -= withdrawalAmount
        print('-' * 20)
        print('Amount withdrawn from account: %d' % withdrawalAmount)
        print('New Balance : %d' % account['balance'])
        print('Returning to previous menu.')
        sleep(3)
    bankOperation(account)

def reportComplaint(account):
    system('clear')
    print('You selected Report a Complaint')
    print('-' * 20)
    complaint = input('Please state your complaint. \n: ')
    print('Thank you for your input.')
    print('Submitting complaint..')
    account['complaint'] = complaint
    sleep(3)
    print('Returning to previous menu.')
    sleep(3)
    bankOperation(account)

def logout():
    #Clear session
    system('clear')
    print('Logging out and returning to Login screen')
    login()

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

##### ACTUAL BANKING SYSTEM #####

init()
