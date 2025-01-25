import time
import numpy as np
numbers = []
start_time = time.time()
random_numbers = np.random.randint(0,1001, size=10**9)
end_time=time.time()
print("the script lasted:",round(end_time-start_time,2))
# finishes 1 bil in 3.52 secomds (more or less)
