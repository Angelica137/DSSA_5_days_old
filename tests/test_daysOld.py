from scripts.daysOld import isLeapYear


def test_isLeapYear_returns_366_if_year_divisible_by_4():
    assert isLeapYear(2004) == 366


def test_isLeapYear_returns_364_if_year_not_divisible_by_4():
    assert isLeapYear(2003) == 365


def test_isLeapYear_returns_365_if_year_divisible_by4_by100():
    assert isLeapYear(1900) == 365


def test_isLeapYear_returns_366_if_year_divisible_by4_by100_and400():
    assert isLeapYear(2000) == 366
