from turtle import *
setup(800,600)
penup()
pendown()
pensize(3)
color('red')
t=input()
t=int (t)
for i in range(100):
    fd(t)
    left(90)
    t=t+10
penup()
goto(0,0)
pendown()
t=10
color('green')
pensize(2)
seth(180)
for i in range(80):
    fd(t)
    right(45)
    t=t+5
penup()
goto(0,0)
pendown()
t=10
color('blue')
pensize(1)
seth(0)
for i in range(80):
    fd(t)
    left(45)
    t=t+5
