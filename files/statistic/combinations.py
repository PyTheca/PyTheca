# help

def Explain():
    text = "This is the combinations function."
    return text




# questions

def Questions(): 
    q = ['Enter n: ', 'Enter k: ']
    return q




# function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def Execute(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))
