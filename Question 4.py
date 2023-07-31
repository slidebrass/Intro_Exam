#Question 4
"""Write a function to return if the given year is a leap year. A leap
    year is divisible by 4, but not divisble by 100, unless it is also
    divisible by 400. The return should be boolean Type (true/false)."""
def is_leap_year(a_year):
    a_year = int(a_year)
    
    if (a_year >= 400) and (a_year % 400 == 0):
            return True
    elif a_year >= 100:
        if (a_year % 4 == 0) and (a_year % 100 != 0):
            return True
    elif a_year >= 4:
        if (a_year % 4 == 0):
            return True
        else:
            return False

leap_year = input("Please enter a year, and I will tell you if it " +
                         "is a leap year. ")
message_yes = "Yes, this is a leap year."
message_no = "No, I'm sorry. This is not a leap year."

if is_leap_year (leap_year):
    print(message_yes)
else:
    print(message_no)