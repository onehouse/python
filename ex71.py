'''
编写input()和output()函数输入，输出5个学生的数据记录。
'''


class Student(object):
    name = ""
    age = ""
    score = {"语文": "", "数学": "", "英语": ""}

    def input_student(self):
        self.name = input("输入姓名：")
        self.age = input("输入年龄：")
        for keys in self.score.keys():
            self.score[keys] = input("输入%s分数：" % keys)

    def output_student(self):
        print("姓名：%s" % self.name)
        print("年龄：%s" % self.age)
        for keys, values in self.score.items():
            print("%s分数：%s" % (keys, values))


for i in range(5):
    student = Student()
    student.input_student()
    student.output_student()