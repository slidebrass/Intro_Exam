#Question 1
"""Write a function to print "hello_USERNAME!" USERNAME is the input of 
    the function. The first line of the code has been defined as below."""
def hello_name(user_name):
    print("hello_" + new_name + "!")

new_name = input("What is your username? ")
hello_name(new_name)
print("\n")


#Question 2
"""Write a python function, first_odds that prints the odd numbers 
    from 1-100 and returns nothing."""
def first_odds(odd_range):
    for value in odd_range:
        if value % 2 == 1:
            print (value)
first_odds(range(1, 101))
print("\n")


#Question 3
"""Please write a Python function, max_num_in_list to return the max 
    number of a given list. The first line of the code has been defined
    as below."""
def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])
num_list = [5, 2, 27, 91]
max_num_in_list(num_list)
print("\n")

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
print("\n")

#Question 5
"""Write a function to check to see if all numbers in a list are consecutive
    numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
    are not consecutive numbers. The reutrn should be boolean Type."""

def is_consecutive(a_list): 
    a_list.sort()
    x = 0
    while x < 4:
        if (a_list[x] + 1) != (a_list[x+1]):
            return False
        x += 1
    return True
        

list_1 = [6,1,7,3,5]
list_2 = [3,2,5,6,4]

if is_consecutive(list_1):
    print(str(list_1) + " is consecutive.")
else:
    print(str(list_1) + " is not consecutive.")

if is_consecutive(list_2):
    print(str(list_2) + " is consecutive.")
else:
    print(str(list_2) + " is not consecutive.")