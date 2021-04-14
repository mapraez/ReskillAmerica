from time import sleep
import os
import validation
import ast

user_db_path = "data/user_record/"


def create(user_account_number, user_details):
    # create a file
    # name: user_account_number.txt
    # add the user details to the file
    # return True
    # if saving file details fails, then delete file
    if does_account_number_exists(user_account_number):
        print("User account number already exists")  # TODO remove
        sleep(2)
        return False
    if does_email_exist(user_details['email']):
        print("User with this Email already exists: " + user_details['email'])
        sleep(2)
        return False

    completion_state = False
    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")
        print("Creating Account..")
        sleep(1)
    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        print("User already exists")
        if not does_file_contain_data:
            delete(user_account_number)
        # print out error, and return False
        # check contents of file before deleting
    else:
        f.write(str(user_details))
        f.close()
        completion_state = True
    finally:
        return completion_state


def read(user_account_number):
    # find user with account number
    # fetch contents of the file
    is_valid_account_number = validation.account_number_validation((user_account_number))
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")
    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid account number type")
    else:
        # Reading raw text from user_file
        user_details_raw = f.readline()
        f.close()
        # converting to dictionary
        user_details = ast.literal_eval(user_details_raw)
        return user_details


def update(account):
    # find user with account number
    # fetch contents of the file
    # update contents of the file
    # save the file
    # return True
    print("Updating Account")
    sleep(1)
    # try:
    with open(user_db_path + str(account['account_number']) + '.txt', 'w') as f:
        f.write(str(account))
    print('Account Updated')
    sleep(1)
    return True
    # except Exception as e:
    #     # Leaving this for now to catch unknown errors # TODO remove when completed
    #     print('Error: ' + str(type(e)))
    sleep(1)


def delete(user_account_number):
    # find user with account number
    # delete the record
    # return True
    print("delete user record")
    is_delete_successful = False
    try:
        os.remove(user_db_path + str(user_account_number) + ".txt")
        is_delete_successful = True
    except FileNotFoundError:
        print("User not found")
    finally:
        return is_delete_successful


def does_email_exist(email):
    # Lists all user .txt files
    all_users = os.listdir(user_db_path)
    # Iterate through list of user_files
    for user_file in all_users:
        # Concatenates path and user_file
        with open(user_db_path + user_file, 'r') as user:
            # Reads file as a basic Python type, saved as user_details
            # user_details is a Dictionary
            user_details = ast.literal_eval(user.read())
            # checking user_details for matching 'email' key
            if user_details['email'] == email:
                return True
    return False


def does_account_number_exists(user_account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(user_account_number) + '.txt':
            return True
    return False


def authenticated_user(user_account_number, password):
    if does_account_number_exists(user_account_number):
        user_details = read(user_account_number)
        if password == user_details['password']:
            print('Login Successful')
            sleep(1)
            return user_details
    return False


# Recreates admin account at runtime if does not exist
account = {'account_number': 1, 'first_name': 'System', 'last_name': 'Admin', 'password': 'SystemAdmin', 'email': 'admin@system.com', 'balance': 0}
if not read(1):
    create(1, account)

# account = {'account_number': 1, 'first_name': 'System', 'last_name': 'Admin', 'password': 'SystemAdmin', 'email': 'admin@system.com', 'balance': 123}
# update(account)
