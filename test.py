import turtle as t

t.pensize(3)
t.speed(10)

t.penup()
t.goto(-200, -50)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(40, steps=3)
t.end_fill()

t.penup()
t.goto(-100, -50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(40, steps=4)
t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.color('green')
t.circle(40, steps=5)
t.end_fill()

t.penup()
t.goto(100, -50)
t.pendown()
t.begin_fill()
t.color('yellow')
t.circle(40, steps=6)
t.end_fill()

t.penup()
t.goto(200, -50)
t.pendown()
t.begin_fill()
t.color('purple')
t.circle(40)
t.end_fill()

t.penup()
t.goto(-100, 50)
t.pendown()
t.color('green')
t.write('Cool Colorful Shapes', font=('Times', 18, 'bold'))

t.hideturtle()

t.done()
