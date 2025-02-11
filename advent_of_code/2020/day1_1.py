import numpy as np
from itertools import combinations

input = open("./inputs/day1.txt", "r").read().split("\n")
input_list = [int(nr) for nr in input]

comb_list = list(combinations(input_list, 2))
mask = np.sum(comb_list, axis=1)
index = [True if item == 2020 else False for item in mask].index(True)
a, b = comb_list[index]
val_match = sum(comb_list[index])
print("sum: ", val_match)
print("result: ", a * b)

print("done")
