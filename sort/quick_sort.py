#!/usr/bin/env python
# encoding: utf-8

class QuickSort(object):

    def __init__(self, lst):
        self.lst = lst

    def partition(self, p, r):
        def partition_1(self, p, r):
            x = self.lst[r]
            i = p - 1
            for j in range(p, r):
                if self.lst[j] <= x:
                    i += 1
                    self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
            self.lst[i+1], self.lst[r] = self.lst[r], self.lst[i+1]
            return i + 1

        def partition_2(self, p, r):
            pass

        return partition_1(self, p, r)


    def quick_sort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self.quick_sort(p, q - 1)
            self.quick_sort(q + 1, r)

def sort_it(lst):
    QuickSort(lst).quick_sort(0, len(lst) - 1)
    return lst

