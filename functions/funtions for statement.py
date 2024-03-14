def acc_user(first_name, last_name):
    print(f'Hi,\n{first_name.capitalize()} {last_name.capitalize()}')
acc_user("CHARLES", "JOHN")
print("_____________________________________")
print()

def get_valid_account_no():
    account_number = " "
    while account_number != -1:
        account_number = int(input("Please enter account number: "))
        if account_number == 220691:
            return account_number
        else:
            print("Invalid account number ")

user_acc_no = get_valid_account_no()
print("Your account number: ", user_acc_no)
print("_____________________________________")
print()

def password_check():
    while True:
        correct_password = "whoop"
        password = input("Please enter your password: ")
        if password == correct_password:
            print("Correct password please continue to your statement")
            break
        else:
            ("Incorrect password! Please enter a valid password: ")

password_check()
print("_____________________________________")
print()


