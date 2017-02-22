#!/usr/bin/env python
# encoding: utf-8

def find(lst):

    high = 0
    low = 0
    high_last = 0
    low_last = 0
    s = lst[0]
    s_last = lst[0]
    for i in range(1,len(lst)):
        if s_last < 0:
            high_last = i
            low_last = i
            s_last = lst[i]
        else:
            high_last += 1
            s_last += lst[i]
        if s_last > s:
            s = s_last
            high = high_last
            low = low_last
    return low, high, s

