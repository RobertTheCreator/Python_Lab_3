
# coding: utf-8

# In[5]:

def dug():
    tl.color('Red')
    tl.width(15)
    for i in range (44):
        tl.right(4)
        tl.forward(5)
    tl.end_fill()
def okr(r):
    for i in range (90):
        tl.left(4)
        tl.forward(r)
def goto(a, b):
    tl.penup()
    tl.goto(a, b)
    tl.pendown()


import turtle as tl
tl.shape('turtle')
goto(0, -100)
tl.begin_fill()
okr(10)
tl.color('Yellow')
tl.end_fill()
tl.color('Blue')
goto(-65, 80)
tl.begin_fill()
okr(2)
goto(60, 80)
okr(2)
tl.end_fill()
tl.color('Black')
goto(-5, 80)
tl.right(90)
tl.width(10)
tl.forward(70)
goto(65, 0)
dug()
goto(100000, 0)
for i in range(10000):
    tl.penup()
    tl.pendown()

