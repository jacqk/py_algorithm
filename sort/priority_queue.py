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

    def heap_increase_key(self, i, key):
        try:
            key >= self.array[i-1]:
        except:
            print "new key is smaller than current key"
        self.array[i-1] = key
        while i > 0 and self.array[self.parent(i) - 1] < self.array[i - 1]:
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.array[heap_size-1] = -float("inf")
        self.heap_increase_key(heap_size - 1, key)

def main():
    test = PriorityQueue([1, 2, 3, 4, 5, 6])
    print test.heap_maximum()
    print test.heap_extract_max()
    print test.heap_maximum()
    print test.array
    test.heap_increase_key()
if __name__ == "__main__":
    main()
