# Using Floyd's Tortoise and Hare algorithm to find duplicates in a given list

# Constraints
# length --> n+1
# numbers --> 1 ... n
# only one duplicate but can be repetitive duplicates
# Time complexity < O(n**2)
# cannot modify list
# Space Complexity < O(1)


def find_dup(new_list):
    tortoise = new_list[0]                      # begin at index 0
    hare = new_list[0]                          # begin at index 0

    while True:                                 # traverse until you reach the meeting point for tortoise and hare
        tortoise = new_list[tortoise]           # traverse to next index (index ==> value of previous tortoise)
        hare = new_list[new_list[hare]]         # traverse at double the speed of tortoise (jump two indexes unlike one)
        if tortoise == hare:
            break                               # get out of loop when both of tortoise and hare meet

    ''' The meeting point is not the required result. 
        When we have a duplicate value in the list Traversing the list ends up in a cycle.
        The meeting point is just a point in the cycle.
        The cycle always begins at the duplicate value'''

    ptr_one = tortoise                    # initialise a pointer to the meeting point.This traverses inside the cycle
    ptr_two = new_list[0]                 # initialise a new pointer from index 0 to traverse from beginning of list
    while ptr_one != ptr_two:             # traverse until both the pointers meet at the duplicate value
        ptr_one = new_list[ptr_one]       # traverse one point at a time
        ptr_two = new_list[ptr_two]       # traverse one point at a time

    return ptr_one                        # return the duplicate value

    '''0 cannot be an element of list.
       The meeting point is always at index 0 and hence the result is always the first value
       i.e. the function returns a wrong value'''


ano_list = [5, 3, 1, 4, 1, 2]
print(find_dup(ano_list))
