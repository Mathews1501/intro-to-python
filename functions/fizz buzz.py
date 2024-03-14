def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return "Fizz Buzz"
    
print(fizz_buzz(20))
