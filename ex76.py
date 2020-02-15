'''
编写一个函数，输入n为偶数时，
调用函数求1/2+1/4+...+1/n,当
输入n为奇数时，调用函数1/1+1/3+...+1/n　
'''


def my_sum(n):
    s = 0
    for i in range(0, n, 2):
        if n % 2 == 0:
            s += 1 / (i+2)
        else:
            s += 1 / (i+1)
    return s


print(my_sum(6))