import numpy as np
from itertools import combinations
import time

invalid_number = 144381670
input = open("inputs/day1.txt", "r").read().split("\n")
input_list = [int(nr) for nr in input]

# itertools version:

start_time = time.time()
comb_list = list(combinations(input_list, 3))
mask = np.sum(comb_list, axis=1)
index = [True if item == 2020 else False for item in mask].index(True)
a, b, c = comb_list[index]
val_match = sum(comb_list[index])
print("sum: ", val_match)
print("result: ", a * b * c)
print("numpy version took", (time.time() - start_time), "seconds")
