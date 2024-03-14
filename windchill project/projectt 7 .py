import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print("The wind chill index is", int(round(wci, 0)))



def convertCelsiustoFahrenheit(c):
   f = float(9/5)*c + 32
   return (f)

#user please enter 50
celsius_temp = 50
int(input('Enter the temp in celsius:'))

fahrenheit_temp = convertCelsiustoFahrenheit(celsius_temp)
print("The Fahrenheit equivalent of entered celsius temp is:", fahrenheit_temp)