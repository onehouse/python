'''
写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
'''


def length_of_string(s):
    return len(s)


if __name__ == "__main__":
    s = input("输入一串字符：")
    length_of_s = length_of_string(s)
    print("这串字符的长度为%d。" % length_of_s)