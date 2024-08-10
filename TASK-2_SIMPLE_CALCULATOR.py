# SIMPLE CALCULATOR

import os

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculate():
    num1 = int(input("Enter first number:"))
    for i in operations:
        print(i)

    flag = True
    while flag:
        symbol = input("Pick an operation:")
        num2 = int(input("Enter second number:"))
        cal = operations[symbol]
        output = cal(num1,num2)
        print(f"{num1} {symbol} {num2} = {output}")

        cont = input(f"Enter 'y' to continue with {output} (or) 's' to start again (or) 'x' to exit:").lower()

        if cont == "y":
            num1 = output
        elif cont == "s":
            flag = False
            os.system("cls")
            calculate()
        elif cont == "x":
            flag = False
    print("BYE!!!")

calculate()
