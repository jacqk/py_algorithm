#!/usr/bin/env python
# encoding: utf-8

import numpy as np

def multiply(A, B):
    n = A.shape[0]
    C = np.array([n, n])

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        C
