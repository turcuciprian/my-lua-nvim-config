import numpy as np
import math

input = open("inputs/day3.txt", "r").read()
input_arr = np.array(input.split("\n")).astype("str")[:-1]


def count_trees(slope_arr, right, down=1):
    # calculate how many times the current columns need to be multiplied to cover the rules of the slope
    columns_multiplied_by = math.ceil(len(slope_arr) / int(len(slope_arr[0]) / right))

    # create necessary columns to reach the bottom of the slope
    temp_arr = np.array([row * columns_multiplied_by for row in slope_arr])

    # remove skipped rows if any
    temp_arr = [row for index, row in enumerate(temp_arr) if (index % down) == 0]

    # return number of trees hit
    trees_hit = sum([row[index * right] == "#" for index, row in enumerate(temp_arr)])
    return trees_hit


cases = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for case in cases:
    trees_hit = count_trees(input_arr, right=case[0], down=case[1])
    result *= trees_hit
    print(f"number of trees captured for {case[0]}r>{case[1]}d:", trees_hit)
print("day 3 part 2 result:", result)
inputs/day3.txt
