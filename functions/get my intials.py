def get_my_initials(name):
    initials = name[0:1].upper()
    return initials

first_name = input("Enter your first name: ")
f_name_initial = get_my_initials(first_name)
middle_name = input("Enter your middle name: ") 
m_name_initial = get_my_initials(middle_name)
last_name = input("Enter your last name: ")
l_name_initial = get_my_initials(last_name)

print("Your initials are: " + f_name_initial, m_name_initial, l_name_initial)







