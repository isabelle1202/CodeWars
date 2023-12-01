# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

# Years divisible by 4 are leap years,
# but years divisible by 100 are not leap years.

# Years divisible by 400 ARE leap years.


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
