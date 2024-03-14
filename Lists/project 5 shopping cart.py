#Welcome to the shopping cart program

cart_items = []
items = ""

#Select iteams for the cart then type "quit" after the last item 

while items != "quit":
    items = input('What item would you like to add to the cart? ')

    if items != "quit":
        cart_items.append(items)

print('\n Your items in the cart are:')

for items in cart_items:
    print(items)

#Input prices for each item on your list type 0 after amounts have been allocated to item

price_list = []
amount = -1

while amount != 0:
    amount = int(input('Please enter an amount: '))

    if amount != 0:
        price_list.append(amount)

print("\n Your prices are:")

for amount in price_list:
    print(amount)

total = 0

for amount in price_list:
    total += amount


print(f"\n Your total is : ${total:.2f} ")

print("\n Your shopping list is:")

for i in range(len(cart_items)):
    items = cart_items[i]
    amount = price_list[i]
    print(f"{i+1 }. {items} - ${amount:.2f}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")
cart_items[index + 1] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(cart_items)):
    items = cart_items[i]
    amount = price_list[i]
    print(f"{i+1}. {items} - ${amount:.2f}")

















