#!/usr/bin/env python
# encoding: utf-8

import sort
import matplotlib.pyplot as plt

def init(n):
    test = [2 ** i for i in range(8)]
    return test

def test_sample(test):
    n = []
    times = []
    for item in test:
        item_counter, timing = sort.main(item)
        n.append(item_counter)
        times.append(timing)
    return n, times

def draw(x, y):
    plt.plot(x, y, 'o-')
    plt.xlabel('number')
    plt.ylabel('time')
    plt.show()

def main(n=8):
    n, times = test_sample(init(n))
    draw(n, times)

if __name__ == '__main__':
    main()
