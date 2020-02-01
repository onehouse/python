'''
一个整数，它加上100后是一个完全平方数，再加上168
又是一个完全平方数，请问该数是多少？
'''
import math
a = int(math.sqrt(168))
for j in range(2, a+1, 2):
    if 168 % j == 0:
        i = 168 // j
        m = (i - j)
        n = (i + j)
        if i % 2 == 0 and m % 2 == 0 and n % 2 == 0:
            print((m//2)**2-100)