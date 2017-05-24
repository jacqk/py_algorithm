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
                return self.key
            else:
                return self.left.min()

        def max(self):
            if self.right.key == None:
                return self.key
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
if __name__ == "__main__":
    main()

