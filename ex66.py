'''
输入3个数a,b,c，按大小顺序输出。　
'''

a = int(input("输入第一个数："))
b = int(input("输入第二个数："))
c = int(input("输入第三个数："))
print("这三个数从大到小排列为：")
for i in sorted([a, b, c], reverse=True):
    print(i, end=",")