'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几
个数相加由键盘控制。
'''

a = int(input("输入数字a："))
r = int(input("几个数相加？"))
s = 0
print("s =", end=" ")
a0 = a
for i in range(r):
    if i < r - 1:
        print("%d +" % a, end=" ")
    else:
        print(a, end=" ")
    s = s + a
    a = 10 * a + a0
print("= %d" % s)



