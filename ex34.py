'''
练习函数调用。
(通俗的理解_name_ == '_main_'：假如你叫小明.py，在朋友眼中，
你是小明(_name_ == '小明')；在你自己眼中，你是你自己(_name_ == '_main_')。
if _name_ == '_main_'的意思是：当.py文件被直接运行时，if _name_ == '_main_'
之下的代码块将被运行；当.py文件以模块形式被导入时，if _name_ == '_main_'
之下的代码块不被运行。)
'''


def hello():
    print("hello, world!")


def three_hello():
    for i in range(3):
        hello()


if __name__ == "__main__":
    three_hello()