from scripts.daysOld import isLeapYear


def test_isLeapYear_returns_366_if_year_divisible_by_4():
    assert isLeapYear(2004) == 366
