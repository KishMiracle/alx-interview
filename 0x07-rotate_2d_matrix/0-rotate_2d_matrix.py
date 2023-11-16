#!/usr/bin/python3
"""
Module : Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ 90 degrees clockwise rotation function
    Args:
        matrix (list[[list]]): a 2D matrix
    """
    mat = len(matrix)
    for i in range(int(mat / 2)):
        y = (mat - i - 1)
        for j in range(i, y):
            x = (mat - 1 - j)
            # get current number index
            temp = matrix[i][j]
            # changing the top for left
            matrix[i][j] = matrix[x][i]
            # changing the left for bottom
            matrix[x][i] = matrix[y][x]
            # changing the  bottom for right
            matrix[y][x] = matrix[j][y]
            # changing the right for top
            matrix[j][y] = temp
