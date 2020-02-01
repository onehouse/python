'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

import math
n = int(input("输入一个整数（>2）:"))
print("%d =" % n, end=" ")
while True:
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            n = n // i
            print("%d *" % i, end=" ")
            break
    else:
        print("%d" % n)
        break