#Ask student for their score

Grade = int(input('What is your Grade percentage?'))

if Grade >= 90:
    Letter = "A"
elif Grade >= 80:
    Letter = "B"
elif Grade >= 70:
    Letter = "C"
elif Grade >= 60:
    Letter = "D"
else:
    Letter = "F" 

print(f'Your letter Grade is: {Letter}')

if Grade >= 70:
    print('Congratulation you Passed the Grade Well done!')
else:
    print('Great effort keep trying your best to achieve')

#Stretch challenge 1

sign = ""

last_digit = Grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

print(f'Your grade percentage is: {Letter}{sign}')



        


