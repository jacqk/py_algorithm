#!/usr/bin/env python
# encoding: utf-8

from undirected_graph import Graph

class DepthFirstSearch(object):
    def __init__(self, graph, source):

        self.mark = [False for i in range(graph.v())]
        self.count = 0
        self.dfs(graph, source)

    def dfs(self, graph, source):
        self.mark[source] = True
        self.count += 1

        for v in graph.fetch_adj(source):
            if (not self.marked(v)):
                self.dfs(graph, v)

    def marked(self, v):
        return self.mark[v]

    def count(self):
        return self.count


def main():
    graph = Graph("tineG.txt")
    source = 0

    search = DepthFirstSearch(graph, source)

    for v in range(graph.v()):
        if search.marked(v):
            print v,
    print

    if search.count != graph.v():
        print "Not ",
    print "connected"


if __name__ == "__main__":
    main()
