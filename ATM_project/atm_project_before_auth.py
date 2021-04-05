from datetime import datetime as Date
from os import system
from time import sleep

print('')
print('Welcome to the ATM')
print('Today is ' + Date.now().strftime("%B %d, %Y (%H:%M:%S)"))
print('')

allowedUsers = {'Marco': 'PasswordMarco', 'Mike': 'PasswordMike', 'Guy' : 'PasswordGuy'}
currentBalance = {'Marco': 111, 'Mike': 222, 'Guy': 333}

userTries = 3
while(userTries > 0):
    name = input("What is your Name? \n: ")
    if(name in allowedUsers):
        print('Hello ' + name)
        print('')

        passwordTries = 3
        while(passwordTries > 0):
            password = input("What is your password? \n: ")
            if(password == allowedUsers[name]):
                print('')
                print('Login successful :)')
                
                while(True):
                    system('clear')
                    print('Welcome Back, %s!' % name)
                    print('These are the available options:')
                    print('1. Withdrawal')
                    print('2. Cash Deposit')
                    print('3. Report a Complaint')
                    print('4. Exit')

                    selectedOption = int(input("Please select an option: \n"))
                    system('clear')

                    if(selectedOption == 1):
                        print('You selected option %s, ' % selectedOption + 'Withdrawal')
                        print('-' * 20)
                        print('Your Current Balance is %d' % currentBalance[name])
                        withdrawalAmount = int(input('How much would you like to withdraw? \n: '))
                        if(withdrawalAmount > currentBalance[name]):
                            print('-' * 20)
                            print('Amount exceeds Current Balance, returning to previous menu.')
                            sleep(3)
                        else:
                            system('clear')
                            currentBalance[name] -= withdrawalAmount
                            print('-' * 20)
                            print('Amount withdrawn from account: %d' % withdrawalAmount)
                            print('New Balance : %d' % currentBalance[name])
                            print('Returning to previous menu.')
                            sleep(3)
                            continue
                    elif(selectedOption == 2):
                        print('You selected option %s, ' % selectedOption + 'Cash Deposit')
                        print('-' * 20)
                        print('Your Current Balance is %d' % currentBalance[name])
                        depositAmount = int(input('How much would you like to Deposit? \n: '))
                        currentBalance[name] += depositAmount
                        print('-' * 20)
                        print('Depositing %d into account' % depositAmount)
                        print('New Balance : %d' % currentBalance[name])
                        print('Returning to previous menu.')
                        sleep(3)
                        continue
                    elif(selectedOption == 3):
                        print('You selected option %s, ' % selectedOption + 'Report a Complaint')
                        print('-' * 20)
                        complaint = input('Please state your complaint. \n: ')
                        print('Thank you for your input.')
                        print('Submitting complaint..')
                        sleep(3)
                        print('Returning to previous menu.')
                        sleep(3)
                        continue
                    elif(selectedOption == 4):
                        print('You selected option %s, ' % selectedOption + 'Exit')
                        print('GoodBye.')
                        sleep(3)
                        quit()
                    else:
                        print('Invalid option selected, Please try again')

            else:
                print('Password incorrect.')
                passwordTries -= 1
                if(passwordTries > 0): 
                    print('Please try again')
        else:
            print('Number of tries exceeded, GoodBye')
            break

    else:
        print('Name not found')
        userTries -= 1
        if(userTries > 0):
            print('Please try again')
else:
    print('Number of tries exceeded, GoodBye')


