#!/usr/bin/env python
# encoding: utf-8

import multiply
import matplotlib.pyplot as plt

def init(n):
    return [i for i in range(n)]

def test(n):
    numbers = []
    times = []
    times_st = []
    for item in n:
        number, time, time_st = multiply.main(item)
        numbers.append(number)
        times.append(time)
        times_st.append(time_st)
    return numbers, times, times_st

def draw(x, y, z):
    plt.plot(x, y, 'o-')
    plt.plot(x, z, '.-')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.show()

def main(n):
    numbers, times, times_st = test(init(n))
    draw(numbers, times, times_st)



if __name__ == '__main__':
    main(n=30)
