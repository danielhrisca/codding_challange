#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:46:03 2018

@author: daniel

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""


def problem_2_with_division(numbers):
    product = 1
    for val in numbers:
        product *= val

    return [
        product / val
        for val in numbers
    ]


def problem_2_without_division(numbers):
    size = len(numbers)

    result = []
    for i in range(size):
        product = 1
        for val in numbers[:i]:
            product *= val
        for val in numbers[i+1:]:
            product *= val
        result.append(product)

    for val in numbers:
        product *= val

    return result


assert problem_2_with_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert problem_2_with_division([3, 2, 1]) == [2, 3, 6]
assert problem_2_without_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert problem_2_without_division([3, 2, 1]) == [2, 3, 6]

print('all fine')
