#!/usr/bin/env python
# encoding: utf-8

class BST(object):

    class Node(object):
        def __init__(self, key, val, n):
            self.key = key
            self.val = val
            self.n = n
            self.left = None
            self.right = None

        def add_leaf(self):
            self.left = BST.Node(None, None, 0)
            self.right = BST.Node(None, None, 0)

        def size(self):
            return self.n

        def get(self, key):
            if self.key == None:
                return None
            elif self.key > key:
                return self.left.get(key)
            elif self.key < key:
                return self.right.get(key)
            elif self.key == key:
                return self.val

        def put(self, key, val):
            if self.key == None:
                self.key = key
                self.val = val
                self.n = 1
                self.add_leaf()
                return
            elif self.key > key:
                self.left.put(key, val)
                self.n = self.left.n + self.right.n + 1
                return
            elif self.key < key:
                self.right.put(key, val)
                self.n = self.left.n + self.right.n + 1
                return
            elif self.key == key:
                self.val = val
                return
        def min(self):
            if self.left.key == None:
                return self
            else:
                return self.left.min()

        def max(self):
            if self.right.key == None:
                return self
            else:
                return self.right.max()

        def floor(self, key):
            if self.key == None:
                return None
            elif self.key == key:
                return key
            elif self.key > key:
                return self.left.floor(key)
            r_right = self.right.floor(key)
            if r_right != None:
                return r_right
            else:
                return self.key

        def select(self, rank):
            if self.left.size() + 1 > rank:
                return self.left.select(rank)
            elif self.left.size() + 1 < rank:
                return self.right.select(rank - self.left.size() - 1)
            else:
                return self.key, self.val
        def rank(self, key):
            if self.key == None:
                return 0
            elif self.key == key:
                return self.left.size() + 1
            elif self.key > key:
                return self.left.rank(key)
            elif self.key < key:
                return self.right.rank(key) + self.left.size() + 1

        def deleteMin(self):
            if self.left.key == None:
                return self.right
            else:
                self.left = self.left.deleteMin()
                self.n = self.left.size() + self.right.size() + 1
                return self

        def deleteMax(self):
            if self.right.key == None:
                return self.left
            else:
                self.right = self.right.deleteMax()
                self.n = self.left.size() + self.right.size() + 1
                return self

        def delete(self, key):
            if self.key == None:
                return self
            elif self.key > key:
                self.left = self.left.delete(key)
            elif self.key < key:
                self.right = self.right.delete(key)
            elif self.key == key:
                if self.left.key == None:
                    return self.right
                elif self.right.key == None:
                    return self.left
                else:
                    tmp = self
                    self = tmp.right.min()
                    self.left = tmp.left
                    self.right = tmp.right.deleteMin
            self.n = self.left.size() + self.right.size() + 1
            return self

    def __init__(self):
        self.root = self.Node(None, None, 0)
        self.root.add_leaf()

    def size(self):
        return self.root.size()

    def get(self, key):
        return self.root.get(key)

    def put(self, key, val):
        return self.root.put(key, val)

    def min(self):
        if self.root.key == None:
            return None
        return self.root.min()

    def max(self):
        if self.root.key == None:
            return None
        return self.root.max()

    def floor(self, key):
        if self.root.key == None:
            return None
        return self.root.floor(key)

    def select(self, rank):
        if rank > self.root.n or rank < 0:
            return None
        return self.root.select(rank)
    def rank(self, key):
        if self.root.get(key) == None:
            return None
        return self.root.rank(key)
    def deleteMin(self):
        if self.root.size() < 1:
            return
        return self.root.deleteMin()
    def deleteMax(self):
        if self.root.size() < 1:
            return
        return self.root.deleteMax()
    def delete(self, key):
        if self.size == 0:
            return
        self.root.delete(key)

def main():
    import numpy as np
#    sample = np.arange(100)
#    np.random.shuffle(sample)
    sample = np.random.randint(100, size=30)
    binary_search_tree = BST()
    for item in sample:
        binary_search_tree.put(item, item)
    for i in range(100):
        print binary_search_tree.get(i)
    print binary_search_tree.min(), "  ", min(sample)
    print binary_search_tree.max(), "  ", max(sample)
    print binary_search_tree.floor(50)
    sorted_set = sorted(list(set(sample)))
    print binary_search_tree.select(5), "  ", sorted_set[4]
    print binary_search_tree.select(10), "  ", sorted_set[9]
    print binary_search_tree.select(20), "  ", sorted_set[19]
    for item in sorted_set:
        print binary_search_tree.rank(item)
    print binary_search_tree.rank(101)
    print binary_search_tree.rank(-1)
    print binary_search_tree.min()
    binary_search_tree.deleteMin()
    print binary_search_tree.min()
    print binary_search_tree.max()
    binary_search_tree.deleteMax()
    print binary_search_tree.max()
    binary_search_tree.delete(5)
    binary_search_tree.delete(10)
    binary_search_tree.delete(20)
if __name__ == "__main__":
    main()
