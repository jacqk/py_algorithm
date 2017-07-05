#!/usr/bin/env python
# encoding: utf-8

from heap import Heap

class PriorityQueue(Heap):

    def __init__(self, array):
        Heap.__init__(self, array)

    def heap_maximum(self):
        return self.array[0]

    def heap_extract_max(self):
        try:
            self.heap_size > 0
        except:
            print "heap underflow"

        max = self.array[0]
        self.exchange(0, self.heap_size - 1)
        self.heap_size -= 1
        self.max_heapify(0)
        return max


def main():
    test = PriorityQueue([1, 2, 3, 4, 5, 6])
    print test.heap_maximum()
    print test.heap_extract_max()
    print test.heap_maximum()
    print test.array

if __name__ == "__main__":
    main()
