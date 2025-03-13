print("welcome to the recipe converter,please select a number")
def cups_to_grams(cup,grams):
    return cup * grams

def tablespoon_to_tespoons(tablespoons):
    return tablespoons * 3

def grams_to_cups(gram,cups):
    return gram / cups



def recipe_converter():
    while True:

        print("1. convert cups to grams ")
        print("2. convert table spoons to tea spoons")
        print("3 convert grams to cups")
        print("4. exit")
        num = input("please select a number: ")
        
        if num == "1":
            cups = float(input("enter the number of cups you want: "))
            grams = float(input("enter the grams in per cup: "))
            result = cups_to_grams(cups,grams)
            print(f"you're result is: {result}")

        elif num == "2":
            tablespoons = float(input("please select how many tablespoons you have: "))
            result = tablespoon_to_tespoons(tablespoons)
            print(f"you're result is: {result}")

        elif num == "3":
            gram = float(input("please select the amount of grams you have: "))
            cups = float(input("please select the amount of cups: "))
            result = grams_to_cups(gram,cups)
            print(f"the amount of cups is: {result}")

        elif num == "4":
            print("you are exiting the programme")
            break 

        else:
            ("please select a valid number in the menu")
recipe_converter()