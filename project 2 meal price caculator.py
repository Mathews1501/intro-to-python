#Please enter the follwing information

float(input("The price of the child's meal"))
float(input("The price of the adult's meal"))
int(input('The number of children'))
int(input('The number of adults'))
float(input('The sales tax rate'))

#Child's meal price: $30
#Adult's meal price: $45
#Number of children: 3
#number of adult's: 3
#Sales tax rate: 14%

Child_Meal_Price = ('30')
Adult_Meal_Price = ('45')
Number_of_children = ('3')
Number_of_adults = ('3')
Sale_tax_rate = ('14')

#Desert cookies to be bought with the change
Cookies = (10)

Subtotal = (225.00)
Sales_tax = (31.50)
Total_sales = (256.50)

#Subtotal:
print("\n Your subtotal is:")
print(float(Child_Meal_Price) * int(Number_of_children) + float(Adult_Meal_Price) * int(Number_of_adults))

#Sale tax
print("\n Your sales tax is:")
print(float(Subtotal) * int(Sale_tax_rate) / int(100))

#Total payment
print("\n Your Total payment is:")
print(float(Subtotal) + float(Sales_tax))

#please enter the payment amount:
float(input('What is the payment amount'))

#Payment amount:
Payment_amount = (300)

#Change after payment
print("\n Your change is:")
print(float(Payment_amount) - float(Total_sales))
#Change after payment
Change = (43.50)

#Desert Cookies bought with the change
print(float(Change) - int(Cookies))







