'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

n = input("输入一个数字：")

# 方法一
print("方法一：")
m = "".join(reversed(n))
if m == n:
    print("%s是回文数。" % n)
else:
    print("%s不是回文数。" % n)
print("\n")

# 方法二
print("方法二：")
l = len(n)
for i in range(l//2):
    if n[i] != n[-i-1]:
        print("%s不是回文数。" % n)
        break
else:
    print("%s是回文数。" % n)
    