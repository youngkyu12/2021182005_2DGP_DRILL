import turtle

y = 6
go = 100
while(y > 0):
    
    count = 5
    while(count > 0):
        turtle.forward(100)
        count = count - 1

    turtle.penup()
    turtle.goto(0, -go*(6 - y))
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)

    y = y - 1

turtle.penup()
turtle.goto(0, 0)
turtle.down()
turtle.right(90)

x = 6
go = 100
while(x > 0):
    
    count = 5
    while(count > 0):
        turtle.forward(100)
        count = count - 1

    turtle.penup()
    turtle.goto(go*(6 - x), 0)
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)

    x = x - 1
