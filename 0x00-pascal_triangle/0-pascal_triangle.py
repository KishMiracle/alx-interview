#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    pas = []

    for i in range(n):
        r_List = [1]
        if i == 0:
            pas.append(r_List)
            continue

        k = i - 1
        for j in range(len(pas[k])):
            if j + 1 == len(pas[k]):
                r_List.append(1)
                break
            # adding the result of previous row and col
            res = pas[k][j] + pas[k][j + 1]
            r_List.append(res)
        pas.append(r_List)

    return pas
