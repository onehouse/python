'''
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示。
（即语法：【语句1  if   条件表达式  else  语句2】的嵌套）
'''

score = float(input("请输入您的分数："))
grade = "A" if (score >= 90) else ("B" if score >= 60 else "C")
print("您的等级为" + grade + "。")