#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:46:03 2018

@author: daniel

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    info = {
        'val': root.val,
        'left': 'None' if root.left is None else serialize(root.left),
        'right': 'None' if root.right is None else serialize(root.right),
    }
    return info


def deserialize(info):
    left = None if info['left'] == 'None' else deserialize(info['left'])
    right = None if info['right'] == 'None' else deserialize(info['right'])
    return Node(info['val'], left, right)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print('all fine')
