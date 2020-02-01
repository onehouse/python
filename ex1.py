'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

l = [1, 2, 3, 4]
sum = 0
for i in l:
    for j in l:
        for k in l:
            if (i != j) and (j != k) and (i != k):
                sum += 1
                print(i*100+j*10+k)
print("一共有%d个三位数。" % sum)





