'''
求输入数字的平方，如果平方运算后小于 50 则退出。
'''
print("如果输入数字的平方小于50，程序将结束。")
while True:
    n = int(input("输入一个数字："))
    print("%d的平方为%d。" % (n, n**2))
    if n**2 < 50:
        print("程序结束。")
        break
