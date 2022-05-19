#!/usr/bin/env python3
# day 4 warmup
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

#BEST PRACTICE:
#The main fuction (houses the main body of your code, is the funtion that calls other functions)

def add(num1,num2):
    print("\n" + str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    
def sub(num1, num2):
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))


def main():
    while True:
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input().upper()
        if calc1.upper() == "Q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input().upper()
        if calc2 == "Q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        if operation == "+":
            add(calc1,calc2)
        elif operation == '-':
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry. Restarting...")


 
main()
