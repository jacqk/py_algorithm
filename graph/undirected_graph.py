#!/usr/bin/env python
# encoding: utf-8

class Graph(object):

    def __init__(self, file):
        with open(file) as f:
            self.number_V = int(f.readline())
            self.adj = [set() for x in range(self.number_V)]

            self.number_E = 0
            for i in range(int(f.readline().strip())):
                v, w = [int(x) for x in f.readline().strip().split()]
                self.add_edge(v, w)

    def v(self):
        return self.number_V

    def e(self):
        return self.number_E

    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.number_E += 1

    def fetch_adj(self, v):
        return self.adj[v]

def main():
    graph = Graph('tineG.txt')
    print graph.v()
    print graph.e()
    print graph.fetch_adj(0)

if __name__ == "__main__":
    main()
