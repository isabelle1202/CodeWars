def is_leap_year(year):
    """defines if a gives year is a leap year"""

    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 100 == 0:
        return False
    else:
        return False
