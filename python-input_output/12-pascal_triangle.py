#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []
    res = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(res[i-1][j-1] + res[i-1][j])
        row.append(1)
        res.append(row)
    return res
