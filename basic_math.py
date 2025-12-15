#addition
#soustration
#multiplication
def multiplication(a,b):
    return a*b
#division
def divide(a, b):
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")
#modulo
def modulo(a,b):
    return a % b
#exponentiation
def expo(num):
    from math import exp
    return exp(num)
#binary
number = 10
binary = bin(number)

print(binary)
#hexadecimal