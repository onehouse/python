'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''
l = []
while True:
    x = input("请输入一个数字：（输入end结束）")
    if x != "end":
        x = int(x)
        l.append(x)
    else:
        break
l.sort()
print(l)
