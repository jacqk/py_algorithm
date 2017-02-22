#!/usr/bin/env python
# encoding: utf-8

import numpy as np

def multiply(A, B):
    n = A.shape[0]

    C = np.ndarray([n, n])
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
