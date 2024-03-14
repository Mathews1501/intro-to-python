with open("life-expectancy.csv") as life_exp:
    next(life_exp)
 
    highest_life_expectancy = -1
    lowest_life_expectancy = 1000
    country = " "
    year_choice = " "

    highest_life_expectancy2 = -1
    lowest_life_expectancy2 = 1000
    country2 = " "
    year_choice2 = " "

# please enter the year:
    Which_year = int(input("Please enter the year: "))

    for line in life_exp:
        parts = line.split(",")
        line.strip()

        entity_name = parts[0]
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])

        if life > highest_life_expectancy:
            highest_life_expectancy = life
            country = entity_name
            year_choice = year

        if life < lowest_life_expectancy:
            lowest_life_expectancy = life

        if year == Which_year:
            highest_life_expectancy2 = life
            country2 = entity_name
            year_choice2 = year

        if life < lowest_life_expectancy2:
            lowest_life_expectancy2 = life


#The overall max life expectancy is:
print(f"The overall maximum life expectancy is: {highest_life_expectancy} in {country} in {year_choice}")
print()

#The overall min life expectancy is:
print(f'The overall minimum life expectancy is: {lowest_life_expectancy}')
print()

#The max life expectancy was:
print(f"The max life expectancy for the year: {Which_year} is {highest_life_expectancy2} in {country2}")
print()

#The min life expectancy is: 
print(f"The min life expectancy for the year: {Which_year} is {lowest_life_expectancy2} in {country2}")



        





    


