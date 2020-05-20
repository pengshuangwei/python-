import turtle
colors=['red','gold','white','black']
turtle.setup(650,650,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("violet")
turtle.seth(-50)
for i in range(4):
    turtle.pencolor(colors[i])
    turtle.circle(40,100)
    turtle.circle(-40,100)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(50,180)
turtle.fd(40*2/3)
turtle.done()
