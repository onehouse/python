'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


def reversed_print(s, n):
    if n == 0:
        return "done"
    else:
        print(s[n-1], end="")
    reversed_print(s, n - 1)


s = "abcde"
l = len(s)
reversed_print(s, l)