#!/usr/bin/env python
# encoding: utf-8

class Heap(object):

    def __init__(self, lst):
        self.array = lst
        self.length = len(lst)
        self.heap_size = len(lst)

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def exchange(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.array[r] > self.array[largest]:
            largest = r
        if largest != i:
            self.exchange(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.length / 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.length - 1, 0, -1):
            self.exchange(0, i)
            self.heap_size -= 1
            self.max_heapify(0)

def sort_it(lst):
    Heap(lst).heap_sort()
    return lst

def main():
    test = Heap([1, 2, 3, 4, 5, 6])
    test.heap_sort()
    print test.array

if __name__ == "__main__":
    main()
