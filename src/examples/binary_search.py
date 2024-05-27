# Binary search: method used to find a specific element in a sorted list

# Goal of the exercise: Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order

import math


def binary_search(elements, target):
    left = 0
    right = len(elements) - 1
    while left <= right:
        middle = math.floor(left + (right - left) / 2)
        if elements[middle] == target:
            return middle
        if elements[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return left
