#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from square_multiply_recursive import *
import time


def init(n):
    return np.random.random_integers(1, 100, [n, n])


def main(n):
    var = np.array([0, 0])
    for i in range(80):
        time_cost, time_st, boolean = test(n)
        var = (var * i + np.array([time_cost, time_st])) / (i + 1)
    print "%dx%d finished in %.6f second(%.6f standard), %s" % (n, n, var[0], var[1], boolean)
    return n, time_cost, time_st


def test(n):
    A = init(n)
    B = init(n)
    start_time = time.time()
    st_answer = np.matmul(A, B)
    start_time_1 = time.time()
    result = multiply(A, B)
    finish_time = time.time()
    boolean = True
    for item in (st_answer == result).flatten():
        if item == False:
            boolean = False
            break
#    print st_answer
#    print result
    return (finish_time - start_time_1, start_time_1 - start_time, boolean)


if __name__ == '__main__':
    main(n=128)
