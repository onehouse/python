'''
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
（改为任意行列矩阵相加）
'''

import numpy as np


def matrix_add(matrix01, matrix02):
    m = len(matrix01[:][0])
    n = len(matrix01[0][:])
    matrix = np.zeros([m,n])
    for i in range(m):
        for j in range(n):
            matrix[i][j] = matrix01[i][j] + matrix02[i][j]
    return matrix


matrix_a = np.random.random([3, 3])
matrix_b = np.random.random([3, 3])
matrix_c = matrix_add(matrix_a, matrix_b)
print(matrix_c)
# 验证
print("用numpy中的add方法做验证：")
print(np.add(matrix_a, matrix_b) == matrix_c)

