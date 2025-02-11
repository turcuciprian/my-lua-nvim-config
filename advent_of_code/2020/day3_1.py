import numpy as np
import math

input = open("inputs/day3.txt", "r").read().split("\n")
slope_arr = np.array(input).astype("str")[:-1]
right, down = (3, 1)

columns_multiplied_by = math.ceil(len(slope_arr) / int(len(slope_arr[0]) / right))
temp_arr = np.array([row * columns_multiplied_by for row in slope_arr])
trees_hit = sum([row[index * right] == "#" for index, row in enumerate(temp_arr)])

print("number of trees captured for 3r > 1d", trees_hit)
