import time
import numpy as np
from itertools import combinations


with open("inputs/day9.txt", "r") as f:
    data = f.read().split("\n")[:-1]

step = 25
start_time = time.time()
for i in range(step, len(data),1):
    val = int(data[i])
    relevant_list = [int(item) for item in data[i-step : i]]
    comb_list = list(combinations(relevant_list, 2))
    mask = np.sum(comb_list, axis=1)
    index_matches = val in mask
    if not index_matches:
        print("the value is: ",val)
        break
print(f"took: {time.time()-start_time:0.6f} seconds")
