#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:46:03 2018

@author: daniel

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.

"""


def find(numbers):
    numbers.sort()
    target = 1
    for number in numbers:
        if number <= 0:
            continue
        else:
            if number > target:
                break
            else:
                target += 1
    return target


assert find([3, 4, -1, 1]) == 2
assert find([1, 2, 0]) == 3

print('all fine')
