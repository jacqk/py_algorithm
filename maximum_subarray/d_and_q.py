#!/usr/bin/env python
# encoding: utf-8

def find_max_crossing_subarray(lst, low, mid, high):
    left_sum = -float('inf')
    s = 0

    i = mid
    while i >= low:
        s += lst[i]
        if left_sum < s:
            left_sum = s
            max_left = i
        i -= 1

    right_sum = -float('inf')
    s = 0

    i = mid + 1
    while i <= high:
        s += lst[i]
        if right_sum < s:
            right_sum = s
            max_right = i
        i += 1

    return max_left, max_right, left_sum + right_sum

def find_max_subarray(lst, low, high):
    if low == high:
        return low, high, lst[low]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_max_subarray(lst, low, mid)
        right_low, right_high, right_sum = find_max_subarray(lst, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(lst, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        elif cross_sum >= left_sum and cross_sum >= right_sum:
            return cross_low, cross_high, cross_sum

def find(lst):
    return find_max_subarray(lst, 0, len(lst) - 1)

if __name__ == '__main__':
    test_lst = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -6, -22, 15, -4, 7]
    find(test_lst)
