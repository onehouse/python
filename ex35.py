'''
（稍作了解）文本颜色设置。
书写格式：
     开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m
'''


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
print(bcolors.WARNING + "警告的颜色字体" + bcolors.ENDC)
