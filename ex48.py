'''
数字比较。
'''

m = float(input("输入第一个数字："))
n = float(input("输入第二个数字："))
# 条件运算符
print("使用条件运算符：")
result = "%.3f > %.3f" % (m, n) if m > n else \
    ("%.3f = %.3f" % (m, n) if m == n else "%.3f < %.3f" % (m, n))
print(result)
# if elif else结构
print("使用if elif else结构：")
if m > n:
    print("%.3f > %.3f" % (m, n))
elif m == n:
    print("%.3f = %.3f" % (m, n))
else:
    print("%.3f < %.3f" % (m, n))