#!/usr/bin/env python
# encoding: utf-8


def find(lst):
    maximum = -float('inf')
    length = len(lst)
    high = length - 1
    low = 0
    for i in range(length):
        s = 0
        for j in range(i, length):
            s += lst[j]
            if s > maximum:
                maximum = s
                high = j
                low = i
    return low, high, maximum
