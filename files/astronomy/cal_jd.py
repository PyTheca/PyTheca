import math

# Julian Day
# Input is YYYY, MM, DD, HH, MM, SS.ssssss
# No leading zero in numbers


def cal_jd(items):

    year = items[0]
    month = items[1]
    day = items[2]
    hour = items[3]
    minute = items[4]
    second = items[5]

    date = year * 10000 + month * 100 + day + hour / 24 + minute / 1440 + second / 86400

    if month < 3 :
        year -= 1
        month += 12

    a = int(year / 100)
    b = 0
    
    if date <= 15821005.000000 :  # Julian Calendar
        b = 0
    if date >= 15821015.000000 :  # Gregorian Calendar
        b = 2 - a + int(a / 4)

    JD = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5 + hour / 24 + minute / 1440 + second / 86400

    if date > 15821005.000000 and date < 15821015.000000 :
        JD = "ERROR : this date does not exist"

    return (JD)

# End
