#!/usr/bin/python3
'''
minimum operations
'''


def minOperations(n):

    if not isinstance(n, int):
        return 0

    operations = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n/i)
            operations += i
            i = 1
        i += 1
    return operations
