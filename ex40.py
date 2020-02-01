'''
将一个数组逆序输出。
'''

a = [1, 2, 3, 4, 5]
for i in range(len(a)//2):
    a[i], a[-i-1] = a[-i-1], a[i]
print(a)
