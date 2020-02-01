'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a_0 = a[:]
a_0.append(0)
n = int(input("输入一个数字："))
if n >= a[len(a)-1]:
    a_0[len(a_0)-1] = n
else:
    for i in range(len(a)):
        if n <= a[i]:
            a_0[i] = n
            for j in range(i+1, len(a_0)):
                a_0[j] = a[j-1]
            break
print("插入后的列表为：", a_0)