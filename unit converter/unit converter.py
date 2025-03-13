def cups_to_grams(cups, grams_per_cup):
    return cups * grams_per_cup

def tablespoons_to_teaspoons(tablespoons):
    return tablespoons * 3

def grams_to_cups(grams, grams_per_cup):
    return grams / grams_per_cup

def kg_to_pounds(kg):
    return kg * 2.20462  

def meters_to_feet(meters):
    return meters * 3.28084  

def inches_to_cm(inches):
    return inches * 2.54  

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

def recipe_converter():
    print("Welcome to the Unit Converter! Please select an option.")

    while True:
        print("1. Convert cups to grams")
        print("2. Convert tablespoons to teaspoons")
        print("3. Convert grams to cups")
        print("4. Convert kilograms to pounds")
        print("5. Convert meters to feet")
        print("6. Convert inches to centimeters")
        print("7. Convert Celsius to Fahrenheit")
        print("8. Exit")

        num = input("Please select a number: ")

        if num == "1":
            cups = float(input("Enter the number of cups: "))
            grams_per_cup = float(input("Enter grams per cup: "))
            print("Your result is:", cups_to_grams(cups, grams_per_cup), "grams")

        elif num == "2":
            tablespoons = float(input("Enter the number of tablespoons: "))
            print("Your result is:", tablespoons_to_teaspoons(tablespoons), "teaspoons")

        elif num == "3":
            grams = float(input("Enter the number of grams: "))
            grams_per_cup = float(input("Enter grams per cup: "))
            print("The equivalent in cups is:", grams_to_cups(grams, grams_per_cup))

        elif num == "4":
            kg = float(input("Enter weight in kilograms: "))
            print(kg, "kg is equal to", kg_to_pounds(kg), "pounds")

        elif num == "5":
            meters = float(input("Enter length in meters: "))
            print(meters, "meters is equal to", meters_to_feet(meters), "feet")

        elif num == "6":
            inches = float(input("Enter length in inches: "))
            print(inches, "inches is equal to", inches_to_cm(inches), "cm")

        elif num == "7":
            celsius = float(input("Enter temperature in Celsius: "))
            print(celsius, "°C is equal to", celsius_to_fahrenheit(celsius), "°F")

        elif num == "8":
            print("You are exiting the program. Goodbye!")
            break

        else:
            print("Please select a valid option from the menu.")

recipe_converter()

