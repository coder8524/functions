def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

try:
    number = int(input("Enter a number: "))
    check_even_odd(number)
except ValueError:
    print("Please enter a valid integer.")
