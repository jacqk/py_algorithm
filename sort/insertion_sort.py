#!/usr/bin/env python
# encoding: utf-8

def sort_it(lst):
    for i, item in enumerate(lst):
        key = lst[i]
        j = i
        while j > 0 and key < lst[j - 1]:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = key

