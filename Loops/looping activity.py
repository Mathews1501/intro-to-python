favourite_letter = input('What is your favorite letter?')
word = "commitment"

for letter in word:
    if letter.lower() == favourite_letter.lower():
        print(letter.upper(), end= "")
    else:
        print(letter.lower(), end= "")
print()

for letter in word:
    if letter.lower() == favourite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print() 


