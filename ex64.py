'''
利用ellipse 和 rectangle 画图。
(ellipse即为椭圆)
'''

import tkinter as tk
canvas = tk.Canvas(width=500, height=500)
canvas.pack()
x0 = 250
y0 = 250
for i in range(10):
    canvas.create_oval(x0-200-5*i, y0-100+10*i, x0+200+5*i, y0+100-10*i)
    canvas.create_rectangle(x0-200-5*i, y0-100+10*i, x0+200+5*i, y0+100-10*i)
canvas.mainloop()