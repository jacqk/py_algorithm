#!/usr/bin/env python
# encoding: utf-8

class RBT(object):

    class Node(object):

        def __init__(self, key, color):
            self.key = key
            self.color = None
            self.left = NIL
            self.right = NIL
            self.parent = NIL

    NIL = Node(nil, "B")

    def left_rotate(self, x):
        assert x.right != NIL
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        assert x.left != NIL
        y = x.left
        x.left = y.left
        if y.right != NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, z):
        y = NIL
        x = self.root
        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = NIL
        z.right = NIL
        z.color = 'R'
        self.rb_insert_fixup(z)


