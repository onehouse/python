'''
暂停一秒输出。
'''
import time
dic = {"a": 1, "b": 2, "c": 3, "d": 4}
for keys, values in dic.items():
    time.sleep(1)
    print("%s的值是%f。" % (keys, values))