'''
两个变量值互换。
'''


def my_exchange(a, b):
    a, b = b, a
    return a, b


if __name__ == "__main__":
    a = 1
    b = 2
    print("a = %d, b = %d" % (a, b))
    a, b = my_exchange(a, b)
    print("a、b交换之后：")
    print("a = %d, b = %d" % (a, b))
