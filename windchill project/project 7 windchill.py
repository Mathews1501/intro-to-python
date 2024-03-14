import math

def wind_chill(windchillcal):

    windchillcal = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
    return windchillcal

def convert2fahrenheit(celsius):
    return (9/5) * celsius + 32 

def main():
    celsius = int(input('Enter the temp in celsius: '))
    print('Celsius: , celsius')
    print('Fahrenheit: , convert2fahrenheit (celsius)')


temp = 0
t = " "
v = " "

while temp != 0:
    v = float(input("Enter the speeds: "))
    t = float(input("Enter the temperature: "))

   
    
print(f'At temperature of {t} and wind speed {v}, the wind chill is: {wind_chill}')


