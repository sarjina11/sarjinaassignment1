#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: s
Semester: Fall2024
Description: <fill this in>
'''

import sys

def leap_year(year: int) -> bool:
    """Return True if the year is a leap year"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def mon_max(month: int, year: int) -> int:
    """Return the maximum days in a month, considering leap years for February"""
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    if month == 2 and leap_year(year):
        return 29
    return mon_dict.get(month, 31)  # Default to 31 days for other months

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    '''
    year, mon, day = (int(x) for x in date.split('-'))
    day += 1  # next day

    if day > mon_max(mon, year):
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
    return f"{year}-{mon:02}-{day:02}"

def before(date: str) -> str:
    """Returns previous day's date as YYYY-MM-DD"""
    year, mon, day = (int(x) for x in date.split('-'))
    day -= 1  # previous day
    
    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    
    return f"{year}-{mon:02}-{day:02}"

def usage():
    """Print a usage message to the user"""
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

def valid_date(date: str) -> bool:
    """Check if the date is in a valid YYYY-MM-DD format"""
    try:
        year, mon, day = (int(x) for x in date.split('-'))
        if mon < 1 or mon > 12:
            return False
        if day < 1 or day > mon_max(mon, year):
            return False
        return True
    except ValueError:
        return False

def dbda(start_date: str, step: int) -> str:
    """Given a start date and a number of days into the past/future, return the resulting date"""
    date = start_date
    for _ in range(abs(step)):
        if step > 0:
            date = after(date)
        elif step < 0:
            date = before(date)
    return date

if __name__ == "__main__":
    # process command line arguments
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    if not valid_date(start_date):
        print("Error: Invalid start date.")
        usage()

    try:
        divisor = int(sys.argv[2])
    except ValueError:
        print("Error: The divisor must be an integer.")
        usage()

    if divisor == 0:
        print("Error: Divisor cannot be zero.")
        usage()

    days = round(365 / divisor)  # Divide the year by the given divisor

    print(f"A year divided by {divisor} is {days} days.")
    
    # Call dbda() to get the date before and after
    past_date = dbda(start_date, -days)
    future_date = dbda(start_date, days)

    print(f"The date {days} days ago was {past_date}.")
    print(f"The date {days} days from now will be {future_date}.")
