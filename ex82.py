'''
八进制转换为十进制
'''


def oct2dec(num_string, flag=1):
    s = 0
    if flag == 1:
        for i in range(len(num_string)):
            s += float(num_string[-i-1])*8**i
    elif flag == -1:
        for i in range(len(num_string)):
            s += float(num_string[i])*8**(-i-1)
    return s


octal_num = input("输入一个八进制数：")
s = 0
minus = -1
if octal_num[0] == "-":
    octal_num = octal_num.replace("-", "")
    minus = 1
if "." in octal_num:
    str_list = octal_num.split(".")
    result = oct2dec(str_list[0]) + oct2dec(str_list[1], flag=-1)
else:
    result = oct2dec(octal_num)
print(-minus*result)