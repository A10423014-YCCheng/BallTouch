import time
from tkinter import *
import math
import numpy as np

class Ball:
    def __init__(self, canvas, ltposition, rdposition, edgelen, fillcolor, xydis):  # 類別建構固定--init--(self)其餘參數自行增加
        self.canvasobj = canvas
        self.id = canvas.create_oval(ltposition, rdposition, ltposition + edgelen, rdposition + edgelen, fill=fillcolor)
        # tkinter畫圓canvas.create_oval(x0,y0,x1,y1)會回傳一個球的ID，左上角(x0,y0)跟右下角(x1,y1)
        self.v = np.asarray([xydis])
        self.r = edgelen / 2
        self.w = self.r**2


    def ballMove(self):
        self.canvasobj.move(self.id, self.v[0][0], self.v[0][1])
        self.ballpos = np.asarray([self.canvasobj.coords(self.id)]) #(400.0, 50.0) (x,y)
        self.ballcenter = np.asarray([((self.ballpos[0][0] + self.r), (self.ballpos[0][1] + self.r))])

        if not (winW-self.r) > self.ballcenter[0][0] > self.r:
            self.v[0][0] = -self.v[0][0]
        if not (winH-self.r) > self.ballcenter[0][1] > self.r:
            self.v[0][1] = -self.v[0][1]


def ballTouch(b1, b2):
    # 判斷兩球心距離是否<兩球直徑(兩球碰撞)
    r1 = b1.ballcenter
    r2 = b2.ballcenter
    dist = np.sqrt(np.sum((r1-r2)**2))
    print(r1,r2)
    print(dist)
    print(b1.r+b2.r)

    if dist <(b1.r+b2.r):
        v1 = b1.v
        v2 = b2.v
        m1 = b1.w
        m2 = b2.w
        M = m1+m2

        dv1 = - 2*m2 / M * np.inner(v1-v2, r1-r2) / np.sum((r1-r2)**2) * (r1 - r2)
        dv2 = - 2*m1 / M * np.inner(v2-v1, r2-r1) / np.sum((r2-r1)**2) * (r2 - r1)

        b1.v += dv1
        b2.v += dv2

tk1 = Tk()  # TK一開始只有一個小小的正方形
tk1.title('Hello World')  # 視窗標體
tk1.wm_attributes('-topmost', 1)  # 永遠在畫面最上層

winW = 800
winH = 600
canvas1 = Canvas(tk1, width=winW, height=winH, bg='skyblue')  # 設置畫布
canvas1.pack()  # 把物件放到視窗上，放上後TK就變大了

tk1.update()  # 更新螢幕

xyd1 = (3., 3.)
xyd2 = (3., 2.)
ball1 = Ball(canvas1, 350, 100, 50, 'yellow', xyd1)
ball2 = Ball(canvas1, 350, 400, 60, 'black', xyd2)


while True:
    ball1.ballMove()
    ball2.ballMove()
    tk1.update()
    time.sleep(0.01)

    ballTouch(ball1,ball2)

tk.mainloop()

