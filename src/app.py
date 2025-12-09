import math
def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def divide (a, b):
    return a/b
    
def sub (a,b):
    return a-b

def cos(a):
    radians = math.radians(a)
    return round(math.cos(radians), 4)

def sin(a):
    radians = math.radians(a)
    return round(math.sin(radians), 4)

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
        
    return round(guess, 4)


def naturalLog(x):
    if x <= 0:
        return "Bound Error (Log)"
    return round(math.log(x), 4)
    



