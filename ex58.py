'''
画图，学用rectangle画方形。　
'''

import tkinter as tk
import random
canvas = tk.Canvas(width=500, height=500, bg='green')
canvas.pack()
x0, y0 = 50, 50
delta_x = random.choice(range(450-x0))
delta_y = random.choice(range(450-y0))
canvas.create_rectangle(x0, y0, x0 + delta_x, y0 + delta_y)
canvas.mainloop()