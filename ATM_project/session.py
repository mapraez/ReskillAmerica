import os
from datetime import datetime as Date
from time import sleep

session_folder = 'data/auth_session/'
def start_session(account):
    print('Starting session')
    while True:
        try:
            with open(session_folder + str(account['account_number']) + '.txt', 'x') as f:
                f.write('Session Open at: '+ Date.now().strftime("%m/%d/%Y-(%H:%M:%S)"))
                break
        except FileExistsError:
            os.remove(session_folder + str(account['account_number']) + '.txt')
            continue
        except Exception as e:
            # Leaving this for now to catch unknown errors # TODO remove when completed
            print('Error: ' + str(type(e)))
            sleep(1)
            break
    sleep(1)


def end_session(account):
    print('Ending Session')
    try:
        os.remove(session_folder + str(account['account_number']) + '.txt')
    except FileNotFoundError:
        print('Session File was missing')
        sleep(1)
    except Exception as e:
        # Leaving this for now to catch unknown errors # TODO remove when completed
        print('Error: ' + str(type(e)))
        sleep(1)
    sleep(1)

