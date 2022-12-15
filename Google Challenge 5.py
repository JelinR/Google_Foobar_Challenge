"""
Expanding Nebula
================

You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies. But -- oh no! -- 
one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start monitoring the nebula, but 
unfortunately, just a moment too late to find where the pod went. However, you do find that the gas of the steadily expanding 
nebula follows a simple pattern, meaning that you should be able to determine the previous state of the gas and narrow down 
where you might find the pod.

From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can model it as 
a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its 4 nearby cells, 
specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, and (4) the cell below and to the right 
of it. If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas, then it will also have gas in the next 
state. Otherwise, the cell will be empty in the next state.


For example lets say the previous state of the grid was:
    .0..
    ..0.
    ...0
    0...



To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of cells around 
each cell.  Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, which means this 2x2 block would 
become cell c[0][0] with gas in the next time step:
.O -> O
..

Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], two of the containing cells have 
gas, so in the next state of the grid, c[0][1] will NOT have gas:
O. -> .
.O

Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:
O.O
.O.
O.O

Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell below and 
to the right of them, respectively.

Write a function solution(g) where g is an array of array of bools saying whether there is gas in each cell (the current scan of 
the nebula), and return an int with the number of possible previous states that could have resulted in that grid after 1 time step.  
For instance, if the function were given the current state c above, it would deduce that the possible previous states were p (given 
above) as well as its horizontal and vertical reflections, and would return 4. The width of the grid will be between 3 and 50 inclusive, 
and the height of the grid will be between 3 and 9 inclusive.  The solution will always be less than one billion (10^9).

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.


-- Python cases --
Input:
solution.solution([[True, True, False, True, False, True, False, True, True, False], 
                   [True, True, False, False, False, False, True, True, True, False], 
                   [True, True, False, False, False, False, False, False, False, True], 
                   [False, True, False, False, False, False, True, True, False, False]])

                   0 0 . 0 . 0 . 0 0 .
                   0 0 . . . . 0 0 0 .
                   0 0 . . . . . . . 0
                   0 0 . . . . . . . 0
                   . 0 . . . . 0 0 . .
Output:
11567

Input:
solution.solution([[True, False, True], 
                   [False, True, False], 
                   [True, False, True]])

                   0 . 0
                   . 0 .
                   0 . 0
Output:
4

Input:
solution.solution([[True, False, True, False, False, True, True, True], 
                   [True, False, True, False, False, False, True, False], 
                   [True, True, True, False, False, False, True, False], 
                   [True, False, True, False, False, False, True, False], 
                   [True, False, True, False, False, True, True, True]])

                   0 . 0 . . 0 0 0
                   0 . 0 . . . 0 .
                   0 0 0 . . . 0 .
                   0 . 0 . . . 0 .
                   0 . 0 . . 0 0 0
Output:
254

"""


def num_to_bin(n_list):
    bins = []
    for elem in n_list:
        first_bit = tuple(int(x) for x in format(elem[0], '#04b')[2:])
        second_bit = tuple(int(x) for x in format(elem[1], '#04b')[2:])
        bins.append([first_bit, second_bit])    
    return bins

def pre_row_div(row):
  pres = []
  
  true_check_cols = [(1, 0), (0, 1), (2, 0), (0, 2)]
  next_possibs = [(x, y) for x in [0, 1] for y in [0, 1]]
  false_check_cols = [(x, y) for x in range(4) for y in range(4) if (x, y) not in true_check_cols]
  
  true_bins = num_to_bin(true_check_cols)
  false_bins = num_to_bin(false_check_cols)

  for pos, row_bit in enumerate(row):
    if pos == 0:
        if row_bit == 1: pres = true_bins
        else: pres = false_bins
        continue
    
    curr = []
    for pre_elem in pres:
      for next_possib in next_possibs:
        check_set = [pre_elem[-1], next_possib]
        if check_set in true_bins: next_bit = 1
        else: next_bit = 0

        if next_bit == row_bit: 
          curr.append(pre_elem + [next_possib])
    pres = curr

  nums_pres = []
  for pres_elem in pres:
    first_num = ''.join([str(x[0]) for x in pres_elem])
    second_num = ''.join([str(x[1]) for x in pres_elem])
    num_set = (int(first_num, 2), int(second_num, 2))

    nums_pres.append(num_set)

  return nums_pres


def solution(matrix):
  prevs = []
  matrix_tr = list(zip(*matrix))
  
  for row in matrix_tr:
    row_bin = [1 if x else 0 for x in row]
    prevs.append(pre_row_div(row_bin))

  weight_dict_prev = {x: 1 for x in prevs[0]}
  for row in prevs[1:]:    
    weight_dict_curr = {x: 0 for x in row}
    for prev_elem in weight_dict_prev.keys():
        valid_curr_elems = [x for x in row if x[0]==prev_elem[1]]
        for valid_curr_elem in valid_curr_elems:
            weight_dict_curr[valid_curr_elem] += weight_dict_prev[prev_elem]

    weight_dict_prev = weight_dict_curr.copy()

  total_count = sum(weight_dict_prev.values())
  return total_count



matrix = [[True, False, True], [False, True, False], [True, False, True]]
print(solution(matrix))