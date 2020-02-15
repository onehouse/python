'''
列表排序及连接。
'''

a = [1, 2, 3]
b = [4, 5, 6]
# 排序
a.sort(reverse=True)
print(a)
# 连接(两种方法)
print(a+b)
a.extend(b)
print(a)
