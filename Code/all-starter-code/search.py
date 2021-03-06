#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index > (len(array) - 1):
        return None
    if item == array[index]:
        return index
    
    return linear_search_recursive(array, item, (index + 1))

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    if array[0] == item:
        return 0
    else:
        lower = 0
        upper = (len(array) - 1)
        while lower <= upper:
            mid = (upper + lower) // 2
            if array[mid] == item:
                return mid
            elif item < array[mid]:
                upper = mid - 1
            elif item > array[mid]:
                lower = mid + 1
            else:
                return None
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    left = 0
    right = (len(array) - 1)
    return recursivehelp(array, item, left, right)

def recursivehelp(array, item, left, right):
    mid = (left + right) // 2 
    if left > right:
        return None
    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return recursivehelp(array, item, left, mid - 1)
    elif array[mid] < item:
        return recursivehelp(array, item, mid + 1, right)

    return binary_search_recursive(array, item, left, right)
