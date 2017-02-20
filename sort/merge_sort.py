#!/usr/bin/env python
# encoding: utf-8

def merge(lst, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    lst_1 = []
    lst_2 = []
    for i in range(n1):
        lst_1.append(p + i)
    for i in range(n2):
        lst_2.append(q + i + 1)
    lst_1.append(float("inf"))
    lst_2.append(float("inf"))

    i = 0
    j = 0
    for index in range(r - p + 1):
        if lst_1[i] <= lst_2[j]:
            lst[index] = lst_1[i]
            i += 1
        else:
            lst[index] = lst_2[j]
            j += 1

def merge_2(lst, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    lst_1 = []
    lst_2 = []
    for i in range(n1):
        lst_1.append(p + i)
    for i in range(n2):
        lst_2.append(q + i + 1)

    i = 0
    j = 0
    for index in range(r - p + 1):
        if i == n1:
            for k in range(n2 - j):
                lst[index+k] = lst_2[j]
                j += 1
            break
        elif j == n2:
            for k in range(n1 - i):
                lst[index+k] = lst_1[i]
                i += 1
            break
        elif lst_1[i] <= lst_2[j]:
            lst[index] = lst_1[i]
            i += 1
        else:
            lst[index] = lst_2[j]
            j += 1

def merge_sort(lst, q, r):
    if r > q:
        middle = (q + r) / 2
        merge_sort(lst, q, middle)
        merge_sort(lst, middle+1, r)
        merge_2(lst, q, middle, r)

def sort_it(lst):
    merge_sort(lst, 0, len(lst) - 1)
    return lst
