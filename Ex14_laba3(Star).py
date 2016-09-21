
# coding: utf-8

# In[1]:

def star(n):
    for i in range (n):
        tl.forward(150)
        tl.left(180 -180/n)
        
def goto(a, b):
    tl.penup()
    tl.goto(a, b)
    tl.pendown()

    
import turtle as tl
tl.shape('turtle')
n = int(input())
goto(30, 0)
tl.left(180)
star(n)
for i in range(10000):
    tl.penup()
    tl.pendown()

