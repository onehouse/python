'''
求一个3*3矩阵主对角线元素之和。
'''

import numpy as np
matrix = np.random.random([3, 3])
print("3*3矩阵：\n", matrix)
s = 0
for i in range(3):
            s = s + matrix[i][i]
print("其对角线元素之和为", s)
