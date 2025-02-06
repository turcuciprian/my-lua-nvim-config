import numpy as np
import math

# Part 1
input = open("./aoc-inputs/aoc-2020-day3-input.txt", "r").read()
input_arr = np.array(input.split("\n")).astype("str")[:-1]


def count_trees(slope_arr, right, down=1):
    temp_arr = np.array([])
    columns_multiplied_by = math.ceil(len(slope_arr) / int(len(slope_arr[0]) / right))
    for _, row in enumerate(slope_arr):
        new_row = row * columns_multiplied_by
        temp_arr = np.append(temp_arr, new_row)
    current_right = 0
    trees = 0
    for index, row in enumerate(temp_arr):
        if index % down:
            continue
        if row[current_right] == "#":
            trees += 1
        current_right += right
    return trees


trees = count_trees(input_arr, right=3)
print("number of trees captured for 3x>1v:", trees)
