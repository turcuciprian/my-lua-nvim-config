import time
numbers = []
start_time = time.time()
for i in range(10**9):
    if i == 10**8:
        print('100 mil')
    if i == (10**8)*2:
        print('200 mil')
    if i == (10**8)*5:
        print('500 mil')
        numbers=[]
    if i == (10**8)*8:
        print('800 mil')
    numbers.append(i)
end_time=time.time()
print("the script lasted:",round(end_time-start_time,2))
# takes 1 min and 40 sec (109 seconds)
