'''
画椭圆。
'''

import tkinter as tk
canvas = tk.Canvas(width=500, height=500, bg='white')
canvas.pack()
x0 = 250
y0 = 250
for i in range(10):
    canvas.create_oval(x0-200-5*i, y0-100+10*i, x0+200+5*i, y0+100-10*i)
canvas.mainloop()





