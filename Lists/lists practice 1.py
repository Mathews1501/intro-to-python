friends = []

my_friends = ""

while my_friends != 'end':
    my_friends = input('What is your friends name?')
    if my_friends != "end":
        friends.append(my_friends)
    elif my_friends != 'john':
            print(input("Who else is named john besides your friend?"))

            print(f'Your friends names are: {friends}')


