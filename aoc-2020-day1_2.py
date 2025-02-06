import numpy as np
from itertools import combinations
import time

input = open("./aoc-inputs/aoc-2020-day1-input.txt", "r").read().split("\n")
input_list = [int(nr) for nr in input]

# itertools version:

start_time = time.time()
comb_np_list = list(combinations(input_list, 3))
mask = np.sum(comb_np_list, axis=1)
index = [True if item == 2020 else False for item in mask].index(True)
a, b, c = comb_np_list[index]
val_match = a + b + c
print("result: ", a * b * c)
print("numpy version took", (time.time() - start_time), "seconds")
