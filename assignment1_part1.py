#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week1 assignment, part 1"""


class ListDivideException(Exception):
    """Custom exception class"""


def listDivide(numbers, divide=2):
    """function that takes two parameters
    Args:
        numbers(list): a list of numbers
        divide(integer): a divisor integer
        
    Return:
        The number of elements in the numbers list that are divisible by divide.
    Example:
        >>> listDivide([1,2,3,4,5,])
        2
        >>> listDivide([2,4,6,8,10])
        5
        >>> listDivide([30, 54, 63, 98, 100], divide=10)
        2
    """
    counter = 0
    for number in numbers:
        if number % divide == 0:
            counter += 1
    return counter

def testListDivide():
    """Tests the listDivide function."""
    testa = listDivide([1, 2, 3, 4, 5])
    testb = listDivide([2, 4, 6, 8, 10])
    testc = listDivide([30, 54, 63, 98, 100], divide=10)
    testd = listDivide([])
    teste = listDivide([1, 2, 3, 4, 5], 1)

    tests = (testa, testb, testc, testd, teste)
    while testa == int(2):
        while testb == int(5):
            while testc == int(2):
                while testd == int(0):
                    while teste == int(5):
                        return tests
    else:
        raise ListDivideException('Exception: a number is incorrect')

print testListDivide()
