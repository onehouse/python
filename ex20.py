'''
一球从100米高度自由落下，每次落地后反跳回
原高度的一半；再落下，求它在第10次落地时，
共经过多少米？第10次反弹多高？
'''

h = 100
s = 0
for i in range(10):
    s = s + h
    h = h / 2
print("第10次落地时,共经过%f米,第10次反弹%f米" % (s, h))
