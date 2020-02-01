'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

a = int(input("year:"))
b = int(input("month:"))
c = int(input("day:"))
day = [0,31,28,31,30,31,30,31,31,30,31,30]
sum = c
if ((a % 100 != 0) and (a % 4 == 0)) or (a % 100 ==0):
    leap = 1
else:
    leap = 0
for i in range(12):
    if b > i:
        sum += day[i]
        if i == 2:
            sum += leap
print("it's the " + str(sum) + "th day.")
