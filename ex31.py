'''
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''

letter = input("输入第一个字母：")
if letter == "m":
    print("%s表示星期一。" % letter)
elif letter == "w":
    print("%s表示星期三。" % letter)
elif letter == "f":
    print("%s表示星期五。" % letter)
elif letter == "t":
    letter_second = input("输入第二个字母：")
    if letter_second == "u":
        print("%s%s表示星期二。" % (letter, letter_second))
    elif letter_second == "h":
        print("%s%s表示星期四。" % (letter, letter_second))
    else:
        print("请输入正确的字母！")
elif letter == "s":
    letter_second = input("输入第二个字母：")
    if letter_second == "a":
        print("%s%s表示星期六。" % (letter, letter_second))
    elif letter_second == "u":
        print("%s%s表示星期日。" % (letter, letter_second))
    else:
        print("请输入正确的字母！")
else:
    print("请输入正确的字母！")



