'''
模仿静态变量的用法。
'''

# 此处var是普通局部变量
def varfunc():
    var = 1
    var += 1
    print(var)


for i in range(3):
    varfunc()


# 此处var相当于是static变量
class Static(object):
    var_static = 1

    def varfunc(self):
        self.var_static += 1
        print(self.var_static)


var = Static()
for i in range(3):
    var.varfunc()