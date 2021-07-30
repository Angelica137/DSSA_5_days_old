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
    '''somethign else happns here'''
