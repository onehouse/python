'''
打印出杨辉三角形。
'''
n = int(input("打印几行杨辉三角？\n"))
a = [[0 for i in range(2*n+1)] for i in range(n)]
a[0][n] = 1
for i in range(1, n):
    for j in range(2*n):
        a[i][j] = a[i-1][j-1] + a[i-1][j+1]
for i in range(n):
    for j in range(2*n+1):
        if a[i][j] == 0:
            print(" ", end=" ")
        else:
            print(a[i][j], end=" ")
    print("\n")

