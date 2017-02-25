#!/usr/bin/env python
# encoding: utf-8

import numpy as np

def multiply(A, B):
    n = A.shape[0]

    if n == 1:
        return np.array([[A[0, 0] * B[0, 0]]])
    elif n == 2:
        return np.matmul(A, B)
    else:
        p_split = n / 2
        A_11 = A[:p_split, :p_split]
        A_12 = A[:p_split, p_split:]
        A_21 = A[p_split:, :p_split]
        A_22 = A[p_split:, p_split:]
        B_11 = B[:p_split, :p_split]
        B_12 = B[:p_split, p_split:]
        B_21 = B[p_split:, :p_split]
        B_22 = B[p_split:, p_split:]
        c_11 = multiply(A_11, B_11) + multiply(A_12, B_21)
        c_12 = multiply(A_11, B_12) + multiply(A_12, B_22)
        c_21 = multiply(A_21, B_11) + multiply(A_22, B_21)
        c_22 = multiply(A_21, B_12) + multiply(A_22, B_22)
#        print A_11, A_12, A_21, A_22
#        print B_11, B_12, B_21, B_22

        return np.concatenate((np.concatenate((c_11, c_21), axis=0), np.concatenate((c_12, c_22), axis=0)), axis=1)

if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[1, 2], [3, 4]])
    print multiply(A, B)
