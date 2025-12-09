import math
def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def divide (a, b):
    return a/b
    
def sub (a,b):
    return a-b

def log(a):
    return a

def cos(a):
    return a

def sin(a):
    return a

def square(a):
    return a * a

def squareRoot(a):
    if a == 0:
        return 0
    if a < 0:
        return "Negative sqrt error"
    lastGuess=a/2
    guess=(lastGuess+a/lastGuess)/2

    while(abs(guess-lastGuess)>.000001):
        lastGuess=guess
        guess=(lastGuess+a/lastGuess)/2
        
    return round(guess, 5)


def naturalLog(x):
    if a <= 0:
        return "Bound Error (Log)"
    return round(math.log(a), 5)
    



