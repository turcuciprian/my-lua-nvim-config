import time
import numpy as np
from itertools import combinations

invalid_number = 144381670

with open("inputs/day9.txt", "r") as f:
    data = f.read().split("\n")[:-1]
    data = [int(item) for item in data]

step = 25
start_time = time.time()

for index in range(2,len(data)):
    custom_contiguous_combinations = [data[i:i+index] for i in range(len(data))]
    mask = np.sum(custom_contiguous_combinations[:-index+1], axis=1)
    if invalid_number in mask:
        index_nr = list(mask).index(invalid_number)
        comb = custom_contiguous_combinations[index_nr]
        result = min(comb) + max(comb)
        print(f"result: {result}")
        break

print(f"took: {time.time()-start_time:0.6f} seconds")
