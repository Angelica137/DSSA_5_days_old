from scripts.daysOld import isLeapYear


def test_isLeapYear_returns_366_if_year_divisible_by_4():
    assert isLeapYear(2004) == 366


def test_isLeapYear_returns_364_if_year_not_divisible_by_4():
    assert isLeapYear(2003) == 365
