# import modules

import math
import cmath




# constants

PI = 3.1415926535897932384626433832795028841971693993751058209749445923




# help

def Explain():
    text = "This is a simple module that solves functions."
    return text




# questions

def Questions(): 
    q = ['Enter a function: ', 'Enter initial estimation: ', 'Enter maximum error: ']
    return q




# function

def Execute(func_str, initial_estimation, max_error):
    def f(x):
        return eval(func_str)

    def derivative(f, x, h=1e-6):
        return (f(x + h) - f(x)) / h

    x_n = initial_estimation
    error = float('inf')
    max_iterations = 1000
    iteration = 0

    while error > max_error and iteration < max_iterations:
        f_x_n = f(x_n)
        f_prime_x_n = derivative(f, x_n)
        if f_prime_x_n == 0:
            print("Derivative is zero. Cannot continue.")
            return

        x_n1 = x_n - f_x_n / f_prime_x_n
        error = abs(x_n1 - x_n)
        x_n = x_n1
        iteration += 1

    if iteration == max_iterations:
        return("Root not found within the maximum number of iterations.")
    else:
        return(f"Root: {x_n:.8f} with an error of {error:.8f}")




# Example usage:
# function_string = "x**2 - 4"
# initial_guess = 2.0
# maximum_error = 0.0001

