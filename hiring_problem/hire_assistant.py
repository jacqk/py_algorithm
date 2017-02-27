#!/usr/bin/env python
# encoding: utf-8

import numpy as np

class HireAssistant(object):

    def __init__(self, cand_lst):
        self.candidates = cand_lst
        self.best = 0

    def hire_assistant(self):
        for candidate in self.candidates:
            if candidate > self.best:
                self.best = candidate

    def randomrize(self):
        def permute_by_sort(self):
            length = len(self.candidates)
            p = np.random.randint(1, length ** 3, size=(length,))
            new_order = np.argsort(p)
            self.candidates = self.candidates[new_order]

        def randomrize_in_place(self):
            length = self.candidates.shape[0]
            for index, item in enumerate(self.candidates):
                j = np.random.randint(index, length)
                self.candidates[index], self.candidates[j] = self.candidates[j], self.candidates[index]

        return randomrize_in_place(self)

if __name__ == '__main__':
    test_case = HireAssistant(np.arange(100))
    print test_case.candidates
    test_case.randomrize()
    print test_case.candidates
