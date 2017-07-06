#!/usr/bin/env python
# encoding: utf-8

import random
from quick_sort import *
import time

def init(n):
    items = range(n)
    random.shuffle(items)
    return items

def check(lst):
    for i, item in enumerate(lst):
        if i > 0 and item < lst[i - 1]:
            return False
    return True

def main(n=100):
    lst = init(n)
#    print lst
    start_time = time.time()
    sort_it(lst)
    end_time = time.time()
#    print lst
    time_cost = end_time - start_time
    print "%d items finished in %.6f second, check = %s" %(n, time_cost, check(lst))
    return n, time_cost

if __name__ == '__main__':
    main()
