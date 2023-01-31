import turtle
import math

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    pi = 3.14
    area = 2 * pi + r
    polygon(bob, area, r)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1

    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polygon(t, n, step_length, step_angle)
    t.rt(step_angle/2)


arc(bob, 52, 180)
