'''Problem

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, 
she captured six key memebers of the Bunny Rebellion, and she beat her personal high score in Tetris.  To celebrate, she's 
ordered cake for everyone - even the lowliest of minions! But competition among the minions is fierce, and if you don't cut
exactly equaal slices of cake for everyone, you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms
are not: there are multiple colors, and every minon must get exactly the same sequence of M&Ms. Commander Lambda hates waste
and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.


To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: 
each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise 
(the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, 
returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

'''


'''Approach

1) Split string into list of letters

2) Fix first letter as reference and traverse to find a similar letter

3) If found, assume this as start of a pattern, with previous letters all making a unit

4) To confirm this, list all first pattern letters together and check if all are the same.  Keep doing this for all letters of the pattern.

5) If this is true for all letters of pattern, then we have our answer.  Else, pattern found is wrong.  Return to step two and try finding reference 
    letter at another location for another possible pattern.


'''

def solution(pattern):
    listed_pattern = [x for x in pattern]   #separates string into letters
 
    p0 = listed_pattern[0]                  #takes first letter for comparison in establishing start of pattern

    for i in range(len(listed_pattern)):                                    #going through the letters in string
        if i == 0: continue                                                 #skip first letter as that is already our reference
        j, length = 0, 300                                                  #needed for renewing after each iteration in i

        if listed_pattern[i] == p0:
            length = i
            for j in range(length):
                if i+j == len(listed_pattern): break
                if listed_pattern[i+j] != listed_pattern[j]: break

            

        if j == length-1: 
            count = 0
            for k in range(length):
                count += 1
                check = sorted(listed_pattern[k::length])

                if check[0] != check[-1]: 
                    count = 0
                    break

            if count == length: break

    pieces = str(len(listed_pattern) // length)

    if length == 300 or len(listed_pattern) % length != 0: print('1')
    else: print(pieces)

solution('abcdefgabcdefg')