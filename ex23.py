'''
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''

n = int(input("输入一个数字（以打印出对应的菱形）："))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print("")
for i in range(1, n):
    for j in range(i):
        print(" ", end="")
    for k in range(2*(n-i)-1):
        print("*", end="")
    print("")
