#Secret word puzzle

print('Welcome to the word guessing game!')
print("")

secret = 'legacy'
guess_count = 0
guess = ""
play_again = 'yes'
print("Your hint is _ _ _ _ _ _")

while guess != secret:
    guess = input('What is your guess?')
    guess_count = guess_count + 1

    if guess == secret:
        print("Wow! you guessed it!")
        print(f"It took you {guess_count} guesses to get the secret word")
        play_again = input("Would you like to play again (yes/no)? ")
        print("Thank you for playing word puzzle. see you soon.")
    elif len(guess) != len(secret):
        print("Your hint is _ _ _ _ _ _")
    else:
        print("""Please try another word
count the letter spaces given _ _ _ _ _ _""")
        






