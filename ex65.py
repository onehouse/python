'''
一个最优美的图案。
（题意不明确，且当做自命题综合应用。）
'''

import tkinter as tk
canvas = tk.Canvas(width=500, height=500)
canvas.pack()
x0, y0 = 50, 50
point_xy = [i for i in range(55, 250, 5)]
canvas.create_rectangle(x0, y0, x0+400, y0+400)

for i in range(39):
    canvas.create_line(x0, point_xy[i], point_xy[38-i], y0)
    canvas.create_line(point_xy[i] + 200, y0, x0 + 400, point_xy[i])
    canvas.create_line(x0, point_xy[i] + 200, point_xy[i], y0 + 400)
    canvas.create_line(point_xy[i]+200, y0 + 400, x0 + 400, point_xy[38-i]+200)
canvas.mainloop()