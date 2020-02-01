'''
求100之内的素数。
(改为求区间[m,M]内的素数。)
'''

import math
lower = int(input("输入下界m (m > 1):"))
upper = int(input("输入上界M (M > n)："))
for i in range(lower, upper + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
# tip: for else 结构：如果for后面的循环体在执行过程中没有被break中断，则执行else后面的；否则不执行。