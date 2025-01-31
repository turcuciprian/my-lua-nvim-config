import numpy as np
import math

# Part 1
input = open("input.txt", "r").read()
input_arr = np.array(input.split("\n")).astype("str")[:-1]


def count_trees(slope_arr, right, down=1):
    temp_arr = np.array([])
    columns_multiplied_by = math.ceil(len(slope_arr)/int(len(slope_arr[0])/right))
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

# Part 2

cases = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for case in cases:
    trees = count_trees(input_arr, right=case[0], down=case[1])
    result *=trees
    print(f"number of trees captured for {case[0]}x>{case[1]}v:", trees)
print("part 2 result:", result)
