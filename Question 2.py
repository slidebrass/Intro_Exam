#Question 2
"""Write a python function, first_odds that prints the odd numbers 
    from 1-100 and returns nothing."""
def first_odds(odd_range):
    for value in odd_range:
        if value % 2 == 1:
            print (value)
first_odds(range(1, 101))
