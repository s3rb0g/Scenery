import turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)

#SKY BACKGROUND#

t.penup()
t.goto(-650,400)
t.pendown()

t.color("black", "light blue")
t.begin_fill()
for n in range(2):
    t.fd(1300)
    t.rt(90)
    t.fd(780)
    t.rt(90)
t.end_fill()


#CLOUDS#

t.penup()
t.goto(650,-200)
t.pendown()

t.color("black", "light gray")
t.begin_fill()

for i in range(13):
    t.setheading(90)
    t.circle(50,180)
    
t.setheading(270)
t.fd(180)
t.lt(90)
t.fd(1300)
t.lt(90)
t.fd(178)

t.end_fill()


#SUN#

t.penup()
t.goto(400,370)
t.lt(90)
t.pendown()

t.color("black", "yellow")
t.begin_fill()
t.circle(75)
t.end_fill()

t.penup()
t.goto(370,370)
t.rt(45)
t.pendown()
t.fd(30)

t.penup()
t.goto(330,340)
t.pendown()
t.fd(30)

t.penup()
t.goto(320,310)
t.setheading(180)
t.pendown()
t.fd(30)

t.penup()
t.goto(320,270)
t.lt(35)
t.pendown()
t.fd(30)

t.penup()
t.goto(340,230)
t.lt(20)
t.pendown()
t.fd(30)

t.penup()
t.goto(380,210)
t.lt(20)
t.pendown()
t.fd(30)

t.penup()
t.goto(430,210)
t.lt(30)
t.pendown()
t.fd(30)

t.penup()
t.goto(465,230)
t.lt(20)
t.pendown()
t.fd(30)

t.penup()
t.goto(485,270)
t.lt(20)
t.pendown()
t.fd(30)

t.penup()
t.goto(485,310)
t.lt(45)
t.pendown()
t.fd(30)

t.penup()
t.goto(470,350)
t.lt(45)
t.pendown()
t.fd(30)

t.penup()
t.goto(435,370)
t.lt(15)
t.pendown()
t.fd(25)


#PIPES UP#

t.penup()
t.goto(-500, 400)
t.setheading(270)
t.pendown()

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(250)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(250)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(250)
t.setheading(0)

t.fd(180)
t.rt(90)

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(60)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(60)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(60)
t.setheading(0)

t.fd(180)
t.rt(90)

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(420)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(420)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(420)
t.setheading(0)

t.fd(180)
t.rt(90)

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(360)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(360)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(360)


#PIPES DOWN#

t.penup()
t.setheading(270)
t.fd(780)
t.setheading(90)
t.pendown()

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(190)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(190)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(190)

t.rt(90)
t.fd(180)
t.setheading(90)

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(130)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(130)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(130)

t.rt(90)
t.fd(180)
t.setheading(90)

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(490)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(490)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(490)

t.rt(90)
t.fd(180)
t.setheading(90)

t.color("black", "light green")
t.begin_fill()
for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.fd(300)

t.color("black", "light green")
t.begin_fill()
t.rt(90)
t.fd(30)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(180)

t.lt(90)
t.fd(40)

t.lt(90)
t.fd(30)
t.end_fill()

t.rt(90)
t.fd(300)
