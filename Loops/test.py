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