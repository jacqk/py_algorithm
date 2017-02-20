#!/usr/bin/env python
# encoding: utf-8

def sort_it(lst):
    for index, item in enumerate(lst):
        min_index = find_min(lst, index)
        lst[index], lst[min_index] = lst[min_index], lst[index]
    return lst

def find_min(lst, start):
    min_index = start
    for i in range(start, len(lst)):
        if lst[min_index] > lst[i]:
            min_index = i
    return min_index
