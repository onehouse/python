'''
找到年龄最大的人，并输出。请找出程序中有什么问题。
'''

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
max_index = "li"
for i in person.keys():
    if person[max_index] < person[i]:
        max_index = i
print(max_index, person[max_index])
