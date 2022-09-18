import turtle

counter = 6
go = 100
while(counter > 0):
    
    count = 5
    while(count > 0):
        turtle.forward(100)
        count = count - 1

    turtle.penup()
    turtle.goto(0, -go*(6 - counter))
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)

    counter = counter - 1

turtle.penup()
turtle.goto(0, 0)
turtle.down()
turtle.right(90)

counter = 6
go = 100
while(counter > 0):
    
    count = 5
    while(count > 0):
        turtle.forward(100)
        count = count - 1

    turtle.penup()
    turtle.goto(go*(6 - counter), 0)
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)

    counter = counter - 1
