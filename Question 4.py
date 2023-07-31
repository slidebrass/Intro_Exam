#Question 4
"""Write a function to return if the given year is a leap year. A leap
    year is divisible by 4, but not divisble by 100, unless it is also
    divisible by 400. The return should be boolean Type (true/false)."""
def is_leap_year(a_year):
    a_year = int(a_year)
    message_yes = "Yes, this is a leap year."
    message_no = "No, I'm sorry. This is not a leap year."
    if a_year >= 400:
        if (a_year % 400 == 0):
            return True
        else:
            return False
    elif a_year >= 100:
        if (a_year % 4 == 0) and (a_year % 100 != 0):
            return True
        else:
            return False
    elif a_year >= 4:
        if (a_year % 4 == 0):
            return True
        else:
            return False
    if True:
        print(message_yes)
    if False:
        print(message_no)
        #no response when given a non-leap year.

leap_message = input("Please enter a year, and I will tell you if it " +
                         "is a leap year. ")

is_leap_year(leap_message)