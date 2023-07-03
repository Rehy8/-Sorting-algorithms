from random import randint
import time

for z in range(5):
    a = [randint(10 ** 6, 10 ** 9) for i in range(10000)]
    start = time.time()
    # here u choose what sort algorithm you want to use
    end = time.time()
    print(a, end - start)
