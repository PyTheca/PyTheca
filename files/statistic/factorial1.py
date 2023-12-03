# help

def Explain():
    text = "This is the factorial function."
    return text




# questions

def Questions(): 
    q = ['Enter a number: ']
    return q




# function

def Execute(n):
    product = 1
    x = 1
    for x in range(1, n+1):
        product *= x
        x += 1
    return product

    
