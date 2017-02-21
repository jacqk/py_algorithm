#!/usr/bin/env python
# encoding: utf-8

import matplotlib.pyplot as plt
import find_max_subarray

def init(n):
    return [2 ** i for i in range(n)]

def test_sample(test):
    n = []
    time = []
    for test_case in test:
        test_n, test_time = find_max_subarray.main(test_case)
        n.append(test_n)
        time.append(test_time)
    return n, time

def draw(x, y):
    plt.plot(x, y, 'o-')
    plt.xlabel('number')
    plt.ylabel('time')
    plt.show()

def main(n=10):
    n, times = test_sample(init(n))
    draw(n, times)
    return n, times

if __name__ == '__main__':
    main()
