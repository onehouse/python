'''输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。'''

s = input("请输入一个字符串：\n")
letters = 0
spaces = 0
digits = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        spaces += 1
    elif c.isdigit():
        digits += 1
    else:
        others += 1
print("这个字符串中共有%d个字母，%d个空格，%d个数字，以及%d个其他字符。" % (letters, spaces, digits, others))


