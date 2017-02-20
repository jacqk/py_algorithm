#!/usr/bin/env python
# encoding: utf-8

def sort_it(lst):
    n = len(lst)
    for i in range(1,n):
        for j in range(n - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
