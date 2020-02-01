'''
对10个数进行排序。
'''

l = []
for i in range(10):
    l.append(int(input("请输入一个数字：")))
# 冒泡排序
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print("冒泡排序：", l)

# 选择排序
for i in range(len(l)):
    min_index = i
    for j in range(i+1, len(l)):
        if l[j] < l[min_index]:
            min_index = j
    if i != min_index:
        l[i], l[min_index] = l[min_index], l[i]
print("选择排序：", l)
