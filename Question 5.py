#Question 5
"""Write a function to check to see if all numbers in a list are consecutive
    numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
    are not consecutive numbers. The reutrn should be boolean Type."""

def is_consecutive(a_list): 
    a_list.sort()
    x = 0
    active = True
    while a_list[x] + 1 == a_list[x+1]:
        x += 1
    else: 
        active = False

list_1 = [6,1,7,3,5]
list_2 = [3,2,5,6,4]

is_consecutive(list_1)
is_consecutive(list_2)