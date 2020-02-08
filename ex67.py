'''
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。　
'''

l = []
while True:
    n = input("输入一个数字：（按空格键结束）")
    if n == " ":
        break
    l.append(int(n))
j = 0
# 找到最大元素的位置
for i in range(1, len(l)):
    if l[i] > l[j]:
        j = i
        i += 1
max_index = j
# 找到最小元素的位置
for i in range(len(l)):
    if l[i] < l[j]:
        j = i
        i += 1
min_index = j
l[0], l[max_index] = l[max_index], l[0]
l[-1], l[min_index] = l[min_index], l[-1]
print(l)