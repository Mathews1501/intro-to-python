shopping_list = []
groceries = 0

while groceries != "quit":
    groceries = input("What are the items for your grocery list?")

    if groceries != "quit":
        shopping_list.append(groceries)

print("\nThe shopping list is:")

for groceries in shopping_list:
    print(groceries)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    groceries = shopping_list[i]
    print(f"{i}. {groceries}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")
shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    groceries = shopping_list[i]
    print(f"{i}. {groceries}")
    
