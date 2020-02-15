'''
求0—7所能组成的奇数个数。
'''

s = 4
for i in range(2, 9):
    print(s)
    s += 4*7*8**(i-2)
print("共组成%d个奇数。" % s)