
# coding: utf-8

# In[2]:

def okr(n):
    for i in range (1, 91):
        tl.left(4)
        tl.forward(n + 3)
    for i in range (90):
        tl.right(4)
        tl.forward(n + 3)
import turtle as tl
tl.shape('turtle')
tl.speed(100)
tl.left(90)
n = int(input())
for i in range (n):
       okr(i)

