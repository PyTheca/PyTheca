# import modules

import cmath

# help

def Explain():
    text = "This is a self defined function ; input is the number a ; output is squareroot of this number."
    return text



# questions

def Questions(): 
    q = ['Enter a number: ']
    return q



# function

def Execute(x):

    a = float(x)
    b = 1
    c = a
    d = (b+c)/2

    while (d*d-a) >= 0.00000000000001:
            c = a/b
            d = (b+c)/2
            b = d

    return (b)
