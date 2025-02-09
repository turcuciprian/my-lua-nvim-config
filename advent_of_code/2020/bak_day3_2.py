import numpy as np
import math

# Part 1
input = open("inputs/day3.txt", "r").read()
input_arr = np.array(input.split("\n")).astype("str")[:-1]


def count_trees(slope_arr, right, down=1):
    temp_arr = np.array([])
    columns_multiplied_by = math.ceil(len(slope_arr) / int(len(slope_arr[0]) / right))
    temp_arr = np.array([row*columns_multiplied_by for row in slope_arr])
#    trees = 0
#    for index, row in enumerate(temp_arr):
#        if index % down:
#            continue
#        if row[current_right] == "#":
#            trees += 1
#        current_right += right
    trees_hit = sum([row[index*right] == "#" for index, row in enumerate(temp_arr)if index % down == 0])
    return trees_hit

cases = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for case in cases:
    trees = count_trees(input_arr, right=case[0], down=case[1])
    result *= trees
    print(f"number of trees captured for {case[0]}x>{case[1]}v:", trees)
print("day 3 part 2 result:", result)
