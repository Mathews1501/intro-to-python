pick_a_number = []
number = -1

while number != 0:
    number = int(input('Please enter a number:'))

    if number != 0:
        pick_a_number.append(number)

print("\n You picked the following numbers:")

for number in pick_a_number:
    print(number)

total = 0

for number in pick_a_number:
    total += number

print(f"\n Your total is : {total} ")

count = len(pick_a_number)
average = total / count

print(f'\n The average is: {average}')

best_so_far = -3

for number in pick_a_number:
    if number > best_so_far:
        best_so_far = number

print(f'\n The largest number is: {best_so_far}')

smallest_so_far = 999999999999

for number in pick_a_number:
    if number > 0 and number < smallest_so_far:
        smallest_so_far = number

print(f'\n The smallest positive number is: {smallest_so_far}')

sorted_list = sorted(pick_a_number)

print('\n The sorted list is: ')

for number in sorted_list:
    print(number)

    



