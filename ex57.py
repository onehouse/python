'''
画图，学用line画直线。
（画出回形图案）
'''

import tkinter as tk
canvas = tk.Canvas(width=500, height=500, bg='green')
canvas.pack()
x0, y0 = 50, 50
l, d = 400, 5
while l >= d:
    l -= d
    canvas.create_line(x0, y0, x0 + l, y0)
    l -= d
    canvas.create_line(x0 + l + d, y0, x0 + l + d, y0 + l + 2*d)
    l -= d
    canvas.create_line(x0 + l + 2*d, y0 + l + 3*d, x0 + 2*d, y0 + l + 3*d)
    l -= d
    canvas.create_line(x0 + 2*d, y0 + l + 4*d , x0 + 2*d, y0 + 2*d)
    x0 += 2*d
    y0 += 2*d
canvas.mainloop()
