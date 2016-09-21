
# coding: utf-8

# In[8]:

def okr():
    for i in range (44):
        tl.right(4)
        tl.forward(3)
    for i in range (46):
        tl.right(4)
        tl.forward(0.5)
        
import turtle as tl
tl.shape('turtle')
tl.left(90)
tl.penup()
tl.pendown()
n = int(input())
print(n)
for i in range (n):
    okr()

