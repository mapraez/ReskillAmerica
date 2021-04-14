import re

def account_number_validation(account_number):
    # Check if input is empty
    # is account number 10 digits
    # input is an integer
    if account_number:
        try:
            int(account_number)
            if int(account_number) == 1:
                return True
            if len(str(account_number)) == 10:
                return True
            else:
                print("Account Number must be 10 Digits")
        except ValueError:
            return False
        except TypeError:
            return False

    return False

def email_validation(email):
    email_regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,6}$"
    if re.search(email_regex, email):
        return True
    return False


