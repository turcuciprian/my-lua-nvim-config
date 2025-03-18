import time
import numpy as np

with open("inputs/day10.txt") as f:
    # splitting by line
    data = f.read().split("\n")
    # sorting ascendingly and converting to int
    data = np.sort(np.array([0, *data], dtype=int))
    data = np.array([*data, data[-1]+3])
star_time = time.time()
jolt_differences = np.array(
    [int(data[i + 1] - data[i]) for i in range(len(data)) if len(data)-1 > i]
)
ones = int(np.sum(jolt_differences == 1))
threes = int(np.sum(jolt_differences == 3))
print(f"result: {ones * threes}")
print(f"Lasted: {time.time()-star_time:0.5f} seconds")

