import turtle

patrat = input('Doriti sa desenati un patrat da/nu: ')

if patrat =='da':
    turtle.shape('turtle')

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
else:
    print('Pana data viitoare!')

turtle.exitonclick()