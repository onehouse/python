'''
判断101-200之间有多少个素数，并输出所有素数。
'''

import math
sum = 0
for i in range(101,201,2):
    k = int(math.sqrt(i))
    for j in range(2,k+1):
        if i % j == 0:
            break
        elif j == k:
            print(i)
            sum += 1
print("一共有%d个素数。"%sum)



