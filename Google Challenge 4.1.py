'''Problem

Distract the Trainers
=====================

The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching 
the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday 
device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. 
And thumb wrestling.

The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their 
bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you 
will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the 
pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose 
interest and go back to supervising the bunny workers, and you don't want THAT to happen!

For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas
wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back 
to training bunnies.

How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 
1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!

Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible 
number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.

The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 
(i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0

-- Java cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
Solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0
'''

def avoid_list(sum_val):
    a = sum_val//4
    b = 3*a
    alist = [(a, b)]

    for elem in alist:
        first_elems, sec_elems = [x[0] for x in alist], [x[1] for x in alist]

        if elem[0] % 2 == 0 and elem[0] // 2 not in first_elems:
            a = elem[0] // 2
            b = elem[1] + a
            alist.append((a, b))

        if elem[1] % 2 == 0 and elem[1] // 2 not in sec_elems:
            b = elem[1] // 2
            a = elem[0] + b
            alist.append((a, b))

    return alist

def check(i, j):
    sum_ij = i+j
    #print(f'i: {i}, j: {j}, sum: {sum_ij}')
    if i == j: return False

    elif sum_ij % 4 != 0: return True

    elif sum_ij % 4 == 0 and ( (sum_ij & sum_ij-1) != 0 ):
        if (sum_ij//4) % 2 != 0 and ( i != sum_ij//4 and i != 3*(sum_ij//4) ): return True     #Odd condition

        elif (i, j) not in avoid_list(sum_ij): return True      #Even condition

    return False

def pairs(x):
    x = sorted(x)
    change = 0

    ci = change = 0
    length = len(x)

    initial = x[ci]
    while x and ci<len(x):        
        initial = x[ci]

        for ipair in x[ci+1:]:
            #print(f'initial: {initial}, pair: {ipair}, x: {x}')
            if check(initial, ipair):
                x.remove(initial)
                x.remove(ipair)
                change = 1
                break

        ci += 1
        if change == 1: ci = 0
        change = 0
        #print(f'x: {x}\n')
    
    return len(x)
            

print(pairs([1, 1, 2, 3, 4]))