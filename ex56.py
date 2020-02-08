'''
画图，学用circle画圆形。
（改为在一张图上随机画任意多的圆。）
'''

import tkinter as tk
import random
window = tk.Tk()
window.title("my window")
window.geometry("700x600")
canvas = tk.Canvas(width=700, height=450, bg='green')
canvas.pack()


def draw_circle_0():
    delta = random.choice(range(225))
    x0, y0 = random.choice(range(delta, 700-delta)), random.choice(range(delta, 450-delta))
    canvas.create_oval(x0-delta, y0-delta, x0+delta, y0+delta)


def draw_circle_1():
    x0, y0 = random.choice(range(10, 700-10)), random.choice(range(10, 450-10))
    canvas.create_oval(x0-10, y0-10, x0+10, y0+10)


b1 = tk.Button(window, text='画圆（任意大小）', command=draw_circle_0)
b1.pack()
b2 = tk.Button(window, text='画圆（定半径）', command=draw_circle_1)
b2.pack()
window.mainloop()





