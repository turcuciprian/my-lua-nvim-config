import time
import numpy as np

with open("inputs/day10.txt") as f:
    # splitting by line
    data = f.read().split("\n")
    # sorting ascendingly and converting to int
    data = np.sort(np.array([0, *data], dtype=int))
    # converting to a np array and making the last item as per requirements +3 jolts than the previously sorted bigger
    data = np.array([*data, data[-1]+3])

star_time = time.time()
#extract the differences between the numbers
jolt_differences = np.array(
    [int(data[i + 1] - data[i]) for i in range(len(data)) if len(data)-1 > i]
)
#calculate the ones in the list
ones = int(np.sum(jolt_differences == 1))
# calculate the 3's in the list
threes = int(np.sum(jolt_differences == 3))
#show the results
print(f"result: {ones * threes}")
print(f"Lasted: {time.time()-star_time:0.5f} seconds")

