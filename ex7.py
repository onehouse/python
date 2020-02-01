'''
将一个列表的数据复制到另一个列表中。
'''
l = []
while True:
    a = input("输入一个数字：（输入end结束）")
    if a != "end":
        l.append(int(a))
    else:
        break
cop = l[:]
print("输入列表：", l, "\n", "复制列表：", cop)
key = int(input("修改输入列表中第几位？"))
value = int(input("把这一位修改为多少？"))
l[key-1] = value
print("输入列表：", l, "\n", "复制列表：", cop)



