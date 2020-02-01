'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

n = input("输入一个不多于5位的正整数：")
# 方法一(将正整数看作字符串)
print("方法一：")
print("该正整数的位数为%d" % len(n))
print("逆序打印该数字：" + "".join(reversed(n)))
print("\n")

# 方法二（分解数字）
print("方法二：")
n = int(n)
a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 // 10
e = n % 10
if a:
    print("该正整数的位数为5")
    print("逆序打印该数字：%d%d%d%d%d" % (e, d, c, b, a))
elif b:
    print("该正整数的位数为4")
    print("逆序打印该数字：%d%d%d%d" % (e, d, c, b))
elif c:
    print("该正整数的位数为3")
    print("逆序打印该数字：%d%d%d" % (e, d, c))
elif d:
    print("该正整数的位数为2")
    print("逆序打印该数字：%d%d" % (e, d))
elif e:
    print("该正整数的位数为1")
    print("逆序打印该数字：%d" % e)




