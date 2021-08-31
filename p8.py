import turtle
import math
import threading
import time

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()


pen1.color('blue')
pen2.color('red')

def go_to(p,x,y):
    p.up()
    p.goto(x,y*100)
    p.down()



def draw_sin(p,angle):
        p.goto(angle,math.sin(math.radians(angle))*100)

def draw_cos(p,angle):
        p.goto(angle,math.cos(math.radians(angle))*100)  


def two_turtle(p1,p2):
    go_to(p1,-360,math.sin(math.radians(-360)))
    go_to(p2,-360,math.cos(math.radians(-360)))
    for i in range(-360,361):
        draw_sin(p1,i)
        draw_cos(p2,i)


two_turtle(pen1,pen2)
