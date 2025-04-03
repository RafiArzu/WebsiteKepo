import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
for i in range (180):
    t.speed(0)
    t.color('#FFB8E0')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('#FFEDFA')
    t.circle(190 - i, 90)
    t.left(18)