#Buck & Marley's Great escape from Kuvukiland

#While one of their great adventures Buck stumbles upon an old relic,
#as he is analyzing this relic he, with great excitement he,
#then calls upon his best friend and co traveller to see the what he has found,
#while they are amazed 
#at what they have found Marley rubs the relic to wipe of the dust,
#which triggering it to teleport them to a maze called kuvukiland
#a land of Bones

Escape_route = int(input('Which enternce will you use to lead to an exit from the maze?'))

#Level 1

if Escape_route <= 1:
    route = 'SHORT'
elif Escape_route == 2: 
    route = 'CHALLENGING' 
elif Escape_route == 3:
    route = 'LONG'
elif Escape_route == 4:
    route = 'HARD MODE'
else:
    route = "LEGENDARY MODE"

print(f'your selected route is: {route.lower()}')

if Escape_route == 1:
    print('This is the journey of wonders')
elif Escape_route == 2:
    print('Stay on course, follow the red star')
elif Escape_route == 3:
    print('Follow the red star beware of mimick stars they mislead the traveller')
elif Escape_route >= 4:
    print('Keep a safe distance from chasers the protectors of the artifects')
else:
    print('Bewared and prepared for the challenge collect as many artifacts as you can')

#Level 2

if Escape_route == "Dark Path":
    route = 'SHORT'
elif Escape_route == "Pot of gold": 
    route = 'CHALLENGING' 
elif Escape_route == "Laviathons passage":
    route = 'LONG'
elif Escape_route == "":
    route = 'HARD MODE'
else:
    route = "LEGENDARY MODE"



