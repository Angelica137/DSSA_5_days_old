daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    if year % 4 == 0:
        return 366
    else:
        return 365


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    '''somethign else happns here'''
