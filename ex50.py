'''
输出一个随机数。
'''
import numpy as np
from matplotlib import pyplot as plt
figure = plt.figure()
# 线性同余法（Xn+1=(aXn+c) mod m）生成（0,1）的100000个随机数
a = 214013
c = 2531011
m = 2**32
x = 1
l = []
count_l =[]
for i in range(100000):
    x = (a*x+c) % m
    l.append(x/m)
    print(x/m)
# 验证生成的伪随机数是否均匀
for i in range(10):
    s = 0
    for j in l:
        if i/10 <= j < (i+1)/10:
            s += 1
    count_l.append(s/100000)
print("处于不同区间的伪随机数频率分别为:")
print(count_l)
plt.hist(np.array(l), bins=10)
figure.show()
print("从列表以及图中可以看出，生成的伪随机数分散较均匀。")
