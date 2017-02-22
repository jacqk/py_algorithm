#!/usr/bin/env python
# encoding: utf-8

import time
import random
from d_and_q import *

def init(n):
    lst = range(-n/2, n/2)
    random.shuffle(lst)
    return lst

def check():
    test_lst = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -6, -22, 15, -4, 7]
    low, high, s = find(test_lst)
    print low, high, s
    if low == 7 and high == 10 and s == 43:
        return True
    else:
        return False

def main(n=100):
    print check(),
    start_time = time.time()
    find(init(n))
    finish_time = time.time()
    time_cost = finish_time - start_time
    print "%d items finished in %.6f second" %(n, time_cost)
    return n, time_cost

if __name__ == '__main__':
    main()
