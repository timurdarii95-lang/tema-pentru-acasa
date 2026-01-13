figura = input('Alegeti o figura de mai jos:patrat, romb, triunghi: ')
import turtle


turtle.shape('turtle')
if figura == 'patrat':

 for i in range(4):
    turtle.forward(100)
    turtle.left(90)

elif figura == 'romb':
 for i in range(2):
     turtle.forward(100)
     turtle.left(60)
     turtle.forward(100)
     turtle.left(120)

elif figura == 'triunghi':
 for i in range(3):
    turtle.forward(100)
    turtle.left(120)

else:
    print('ERORR!!!')
turtle.exitonclick()
