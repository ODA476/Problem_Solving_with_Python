import turtle as t

x1, y1 = eval(input('Enter x1, y1: '))
x2, y2 = eval(input('Enter x2, y2: '))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('The distance is: ', distance)

t.penup()
t.goto(x1, y1)
t.pendown()
t.write('point 1')
t.goto(x2, y2)
t.write('point 2')

t.penup()
t.goto((x1 + x2) / 2, (y1 + y2) / 2)
t.write(distance)
t.done()
