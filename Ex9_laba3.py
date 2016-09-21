
# coding: utf-8

# In[20]:

def ris(n):
    tl.left(180 - (n-2)/n*90)
    for i in range (n):
        tl.forward(10*n)
        tl.left(180 - (n-2)/n*180)
    tl.right(180 - (n-2)/n*90)
    
import turtle as tl
tl.shape('turtle')
n = int(input())
a = 9
for i in range (3, n):
    ris(i)
    tl.penup()
    tl.goto(a, 0)
    tl.pendown()
    a += 9

    

