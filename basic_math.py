#addition
def addition(a, b):
    return a + b
#soustration
def soustration(a,b):
    return a-b
#multiplication
def multiplication(a,b):
    return a*b
#division
def division(a, b):
    return a/b
#modulo
def modulo(a,b):
    return a % b
#exponentiation
def exponentiation(a,b):
    return a**b
#binary
def binary(n):
    binary = ''
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary