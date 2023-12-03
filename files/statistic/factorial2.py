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
    if n == 0 or n == 1:
        return 1
    else:
        return n * Execute(n - 1)
        
