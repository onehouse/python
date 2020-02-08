'''
查找字符串。
'''

str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = 'cde'
print("使用find（）方法:")
print(str1.find(str2))
print("\n")
print("自编程序：")
for j in range(len(str1)):
    if str2[0] == str1[j]:
        if str2 == str1[j:j+len(str2)]:
            print("这段字符串位于大字符串的索引%d处。" % j)
    elif j == len(str1)-1:
        print("这段字符串不包含在大字符串之中。")
