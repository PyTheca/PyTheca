import math

# integer

def integer(x):
    y = int(x)
    return(y)

# fraction

def fraction(x):
    y = x - int(x)
    return(y)

# Julian Day to Calendar Date

def jd_cal(jd):

    if jd < 0:
        return("Negative JD not allowed")
        
    if jd >= 0:
        jd_mod = jd + 0.5
        z = integer(jd_mod)
        f = fraction(jd_mod)

        if z < 2299161:
            a = z

        if z >= 2299161:
            alpha = integer((z - 1867216.25) / 36524.25)
            a = z + 1 + alpha - integer(alpha/4)

        b = a + 1524
        c = integer((b-122.1)/365.25)
        d = integer(365.25 * c)
        e = integer((b-d)/30.6001)

        day = b - d - integer(30.6001 * e) + f
        day_integer = int(day)

        hours = integer(fraction(day) * 24)
        minutes = integer(fraction(fraction(day) * 24) * 60)
        seconds = integer(fraction(fraction(fraction(day) * 24) * 60) * 60)

        if e < 14:
            month = e - 1
        if e >= 14:
            month = e - 13

        if month > 2:
            year = c - 4716
        if month <=2:
            year = c - 4715

        datestring = []

        datestring.append(year)
        datestring.append(month)
        datestring.append(day_integer)
        datestring.append(hours)
        datestring.append(minutes)
        datestring.append(seconds)

            
        return(datestring)

# End

