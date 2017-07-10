#!/usr/bin/env python
# encoding: utf-8

def counting_sort(A, k):

    C = [0] * (k + 1)
    for i in range(k + 1):
        C[A[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    B = [None] * len(A)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(len(A)):
        A[i] = B[i]

def sort_it(lst):
    k = max(lst)
    return counting_sort(lst, k)
