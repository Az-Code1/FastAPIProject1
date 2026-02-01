import math


def __init():
    print("Welcome to the most awesome calculator that performs operations on two numbers.\n")

def take_input():
    choiced = input("Please select the type of operation you would like to perform: \n"
                   "Enter 1 for addition\n"
                   "Enter 2 for subtraction\n"
                   "Enter 3 for multiplication\n"
                   "Enter 4 for division\n"
                   "Enter 5 for square\n"
                   "Enter 6 for square_root\n"
                   "Enter 7 for power\n"
                   "Enter 8 for remainder after division\n"
                    "or enter any other character to exit . . . ")
    return float(choiced)


def query():
    decision = input("Do you want to perform another calculation?"
          "\nIf yes enter 1, if no, enter any other thing\n")
    if decision == "1":
        take_input()
    else:
        print("Thank you for using this awesome calculator")

def add(a, b):
    print(f"The sum of two numbers is: {a + b}")
    query()

def subtract(a, b):
    print(f"The result of subtracting b from a is: {a - b}")
    query()

def multiply(a, b):
    print(f"The product of two numbers is: {a * b}")
    query()

def divide(a, b):
    if b == 0:
        print("You cannot divide by zero\n")
        take_input()
    else:
        print(f"The result of dividing a by b is: {a / b}")
        query()

def square(a):
    print(f"Note: input b will be totally ignored and input a will be squared"
          f"The result of calculating the square of a is: {a ** 2}")
    query()

def square_root(a):
    print(f"The result of calculating a to the square root of b is: {math.sqrt(a)}\n")
    query()

def power(a, b):
    print(f"The result of calculating a to the power of b is: {a ** b}")
    query()

def remainder(a, b):
    print(f"The remainder when divide a by b is: {a % b}")
    query()

try:
    choice = float(take_input())
    match choice:
        case 1:
            add(float(input("Please enter the first number you would like to add: \n")),
                float(input("Please enter the second number you would like to add: ")))
        case 2:
            subtract(float(input("Note: The formula to use is a-b.\n Please enter a: \n")),
                float(input("Please enter b: ")))
        case 3:
            multiply(float(input("Please enter the first number you would like to multiply: \n")),
                float(input("Please enter the second number you would like to multiply: ")))
        case 4:
            divide(float(input("Note: The formula to use is a/b.\nNote: b should not be zero\n Please enter a: \n")),
                float(input("Please enter b: ")))
        case 5:
            square(float(input("Enter the number you want to square: ")))
        case 6:
            square_root(float(input("Enter the number you want to square root: ")))
        case 7:
            power(float(input("Please enter the first number you would like to multiply: \n")),
                float(input("Please enter the second number you would like to multiply: ")))
        case 8:
            remainder(int(input("You are just about to get the remainder of a "
                                "number after dividing it with another(the second) number\n"
                                "Note: The formula to use is a/b and the numbers must be whole number.\n"
                                " Please enter a: \n")),
                                int(input("Please enter b: ")))
        case _:
            print("Thank you for using this awesome calculator")
except ValueError:
    print("Please enter a valid number")
    take_input()



