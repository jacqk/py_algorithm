#!/usr/bin/env python
# encoding: utf-8

class Heap(object):

    def __init__(lst):
        self.array = lst
        self.length = len(lst)
        self.heap_size = len(lst)

    def parent(self, i):
        return i / 2

    def left(self, i):
        return i * 2

    def right(self, i):
        return i * 2 + 1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size
