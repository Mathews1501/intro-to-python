import math
  
def WC(t, v):
      
    wc = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
    return wc

def convertCelsiustoFahrenheit(c):
    f = float(9/5)*c + 32
    return (f)

celsius_temp = 30

int(input('Enter the temp in celsius:'))

fahrenheit_temp = convertCelsiustoFahrenheit(celsius_temp)
print("The Fahrenheit equivalent of entered celsius temp is:", fahrenheit_temp)
   
temp = True 
t = " "
v = " "

while temp == True:
    t = float(input("Enter the temperature: "))
    v = float(input("Enter the speed:"))

    print(f"At temperature {t} and wind speed of {v} the wind chill is:", float(round(WC(t, v))))





