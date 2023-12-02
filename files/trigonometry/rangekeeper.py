# help

def Explain():
    text = "This is a self defined rangekeeper function ; input is a number for the input for a repetitive function, the lower limit end the upper limit."
    return text




# questions

def Questions(): 
    q = ['Enter a number: ', 'Enter the lower limit: ', 'Enter the upper limit: ']
    return q




def Execute(number, lowerlimit, upperlimit):
    stretch     = upperlimit - lowerlimit
    corrected_number = (((number - lowerlimit) / stretch) % 1) * stretch + lowerlimit
    
    if corrected_number < 0:
        corrected_number = corrected_number + stretch
    
    return corrected_number    

