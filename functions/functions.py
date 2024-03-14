# #THIS FUNCTION CAN PEFORM A TASK 

def employee_name (first_name, last_name):
    #print(input('What is your Name before we begin this parctise? '))
    print(f'Mr/Mrs {first_name.capitalize()} {last_name.capitalize()}')
    print()
    print('YOUR NEW SALARY WILL BE CALCUTED BASED ON THE 15% ANNUAL INCREASE RATE'.lower().capitalize())
employee_name("Mathews", "Chipeta")
print()

#THIS FUNCTION CONSISTS OF A DEFAULt ARGUMENT
#first method for returing 
def salary_increase(amount, by):
    return amount + by

new_amount = salary_increase(25000, 15/100*25000)
print('Your new salary effect from the 1st of Septemter with 15% I ncrement is:')
print(new_amount)
print()

#Second method for returning using a optional perameter 
def salary (amount, by=15/100*40000):
    return amount + by

print(salary(40000))
print()

#THIS FUNCTION CAN RETURN A VALUe

def my_contact (my_number):
    return f'For any quiries regarding increaments please contact me on the following: {my_number}'

phone_no = my_contact('0684793840')
print(phone_no)