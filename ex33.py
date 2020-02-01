'''
按逗号分隔列表。
'''

l = [1, 2, 3, "a", "b", "c"]
# 方法一
for i in l:
    print(i, end=",")
print("\n")
# 方法二（使用join方法）
print(",".join([str(i) for i in l]))