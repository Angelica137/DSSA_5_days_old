daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    days = 365
    if year % 4 == 0:
        days = 366
        if year % 100 == 0:
            days = 365
            if year % 400 == 0:
                days = 366
    return days


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    if y1 == y2:
        if m1 == m2:
            days = d2 - d1

    elif(y2 - y1 == 1):
        i = 11
        y1_days = 0
        y2_days = 0
        while i > m1-1:
            y1_days += daysOfMonths[i]
            i -= 1
        j = 0
        while m2 > 1:
            print(daysOfMonths[j])
            print(m2)
            y2_days += daysOfMonths[j]
            j += 1
            m2 -= 1

        days_month1 = daysOfMonths[m1 -1] - d1

        days = y1_days + y2_days + days_month1 + d2

        if isLeapYear(y1) == 366 and m1 < 3:
            days += 1
        if isLeapYear(y2) == 366 and m2 > 1:
            days += 1
        
    
    #else:
    #    years = list(range(y1, y2))
    #    for year in years:
    #        if isLeapYear(year) == 366:

    return days


print(daysBetweenDates(2001, 3, 3, 2002, 8, 8))