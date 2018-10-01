#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:46:03 2018

@author: daniel

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""


def problem_1(numbers, target_sum):
    candidates = set()

    for number in numbers:
        if number in candidates:
            return True
        else:
            candidates.add(target_sum - number)

    return False


assert problem_1([10, 15, 3, 7], 17) is True
assert problem_1([10, 15, 3, 7], 20) is False

print('all fine')
