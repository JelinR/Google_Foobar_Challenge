'''Problem
The Grandest Staircase Of Them All
==================================

With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, 
Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks 
(for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with
each amount of bricks, so they can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the 
previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having 
a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly 
n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(3)
Output:
    1

Input:
Solution.solution(200)
Output:
    487067745

-- Python cases --
Input:
solution.solution(200)
Output:
    487067745

Input:
solution.solution(3)
Output:
    1

'''
from functools import reduce 

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def check_factor(n):
    f_list = sorted(list(factors(n)))

    if len(f_list) % 2 == 0: mid = len(f_list)//2
    else: mid = len(f_list)//2 +1

    for f1, f2 in zip(f_list[:mid], reversed(f_list[mid:])):
        if f2 == 3*f1 -1: return True, f1
        elif f2 == 3*f1+1: return True, -f1
    return False, 0

def pent_series(limit):
    initial_vals = []
    count = 1
    for i in range(limit):
        if i%2 == 0: initial_vals.append(count)
        else: 
            initial_vals.append(-count)
            count += 1

    func = map(lambda k: int(k*(3*k-1) / 2), initial_vals)

    return list(func)

def q(k, k_dict):
    #Base cases
    if k in k_dict: return k_dict[k]

    check, m = check_factor(k)
    if check: a = int((-1)**m)
    else: a = 0

    subs = pent_series(k)
    subs = [x for x in subs if k>=x]

    sum = a
    sign = 1
    for count, i in enumerate(subs):
        if count%2 == 0 and count!=0: sign *= (-1)
        sum += sign * q(k - i, k_dict)

    
    if k not in k_dict.keys(): k_dict[k] = sum
    return sum

def solution(num):
    k_dict = {0:1, 1:1, 1:1, 2:1, 3:2, 4:2}
    result = q(num, k_dict)
    return result-1


#print(pent_series(30))
print(solution(200))
#print(factors(25))
#print(check_factor(8))