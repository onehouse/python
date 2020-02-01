'''
按相反的顺序输出列表的值。
'''

l = [1, 2, 3, "a", "b", "c"]
# 方法一
for i in range(len(l)):
    print(l[-i-1], end=",")
print("\n")
# 方法二（切片操作中，步长为负数意味着从右向左切片）
for i in l[::-1]:
    print(i, end=",")