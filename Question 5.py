#Question 5
"""Write a function to check to see if all numbers in a list are consecutive
    numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
    are not consecutive numbers. The return should be boolean Type."""

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