import turtle

turtle.shape('turtle')


for i in range(4):
     turtle.forward(300)
     turtle.left(90)

turtle.penup()
turtle.goto(100,100)

turtle.pendown()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)

turtle.exitonclick()