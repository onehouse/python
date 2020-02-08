'''
有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数。　
'''

initial_l = list(range(1, 20))
for m in range(20):
    print("当m = %d 时：" % m)
    # 第一种方法：使用切片
    final_l1 = initial_l[19-m:] + initial_l[:19-m]
    print(final_l1)
    # 第二种方法：按照要求，逐元素进入空列表
    final_l2 = []
    for i in range(19-m, 19):
        final_l2.append(initial_l[i])
    for i in range(19-m):
        final_l2.append(initial_l[i])
    print(final_l2)
    print("\n")

