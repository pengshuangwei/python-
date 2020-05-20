from turtle import *
setup (800,600)
color('green','yellow')
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
goto(200,0)
seth(-90)

fd(500)
seth(0)
fd(40)
seth(90)
fd(500)
