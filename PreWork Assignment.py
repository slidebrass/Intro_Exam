#Question 1
"""Write a function to print "hello_USERNAME!" USERNAME is the input of 
    the function. The first line of the code has been defined as below."""
def hello_name(user_name):
    print("hello_" + new_name + "!")

new_name = input("What is your username? ")
hello_name(new_name)


#Question 2
"""Write a python function, first_odds that prints the odd numbers 
    from 1-100 and returns nothing."""
def first_odds():
    for value in range(0,100):
        if value % 2 == 1:
            print (value)
first_odds()
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


#Question 4
"""Write a function to return if the given year is a leap year. A leap
    year is divisible by 4, but not divisble by 100, unless it is also
    divisible by 400. The return should be boolean Type (true/false)."""
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0
leap_message = input("Please enter a year, and I will tell you if it " +
                         "is a leap year. ")

is_leap_year(leap_message)

#Question 5
"""Write a function to check to see if all numbers in a list are consecutive
    numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
    are not consecutive numbers. The reutrn should be boolean Type."""

def is_consecutive(a_list): 
    a_list.sort()
    for item in a_list:
        if item


length = len(a_list)