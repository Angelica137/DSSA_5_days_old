from scripts.daysOld import isLeapYear, daysBetweenDates


def test_isLeapYear_returns_366_if_year_divisible_by_4():
    assert isLeapYear(2004) == 366


def test_isLeapYear_returns_364_if_year_not_divisible_by_4():
    assert isLeapYear(2003) == 365


def test_isLeapYear_returns_365_if_year_divisible_by4_by100():
    assert isLeapYear(1900) == 365


def test_isLeapYear_returns_366_if_year_divisible_by4_by100_and400():
    assert isLeapYear(2000) == 366


def test_daysBetweenDates_returns_1_for_1_day_old():
    assert daysBetweenDates(2021, 1, 1, 2021, 1, 2) == 1


def test_daysBetweenDates_returns_523():
    assert daysBetweenDates(2001, 3, 3, 2002, 8, 8) == 523


def test_daysBetweenDates_returns_948():
    assert daysBetweenDates(2000, 1, 3, 2001, 8, 8) == 583


def test_daysBetweenDates_returns_948():
    assert daysBetweenDates(1997, 3, 1, 2021, 7, 31) == 8918