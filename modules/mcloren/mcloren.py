from math import pi

def factorial(n: int):
    a = 1
    for i in range(2, n+1): a *= i
    return a

def exp(x):
    return sum([x**n/factorial(n) for n in range(x+1)])

def sin(x):
    return sum([ ((-1) ** i)*(x ** (2*i + 1)) / factorial(2*i+1) for i in range(x+1) ])

def cos(x):
     return sum( [((-1) ** i)*(x ** (2*i)) / factorial(2*i) for i in range(x+1) ])

def arcsin(x): 
    return sum( [ factorial(2*i) / ( (4**i) * (factorial(i)**2) * (2*i + 1)) for i in range(x+1) ])

def arccos(x):
    return pi/2 - arcsin(x)