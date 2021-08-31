import turtle
pen=turtle.Turtle()
pen.speed(-1)

def square(size=100):
    for i in range(4):
        pen.fd(size)
        pen.lt(90)
def spiral():
    for i in range(2,100,5):
        square(i)

def goto(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()

def polygun(n=3,size=100):
    angle=360/n
    for i in range(n):
        pen.fd(size)
        pen.lt(angle)
    
def polygunD(n=3,size=100,x=0,y=0,color='red'):
    pen.color(color)
    goto(x,y)
    pen.begin_fill()
    polygun(n,size)
    pen.end_fill()

def fourShapes():
    colors=('red',"#ffff00",'darkblue','green')
    pos=((200,200),(200,-200),(-200,200),(-200,-200))
    for i,j in enumerate(colors):
        polygunD(color=j,n=i+3,x=pos[i][0],y=pos[i][1])

def spiral2(n=100):
    for i in range(1,n,2):
        pen.fd(i)
        pen.lt(90)

def spiral3(n=100):
    for i in range(1,n):
        pen.pensize(1+i//10)
        c=1-i/n
        pen.color(c,c,c)
        pen.fd(i)
        pen.lt(90)
def spiral4(n):
    turtle.bgcolor('black')
    colors=('red','orange','yellow','green','skyblue','blue')
    for i in range(n):
        pen.color(colors[i%6])
        pen.fd(i)
        pen.left(57)
        
def spiral5(n):
    from p5 import fibo
    for i in range(2,n):
        pen.pensize(1+i//4)
        pen.circle(fibo( i),90)

def tree():
    import random
    t=random.randrange(256)
    rang=f"#00{t:02x}00"
    sz=int(20+80*t/255)
    x1=random.randrange(-200,200)
    y1=random.randrange(-150,150)
    
    polygunD(n=3,size=sz,x=x1,y=y1,color=rang)
    
def jungle(n):
    for i in range(n):
        tree()

############
def tree2(t):
    import random
    rang=f"#00{t:02x}00"
    sz=int(20+80*t/255)
    x1=random.randrange(-200,200)
    y1=random.randrange(-150,150)
    
    polygunD(n=3,size=sz,x=x1,y=y1,color=rang)
    
def jungle2(n):
    turtle.bgcolor('darkblue')
    import random
    ts=[]
    ts=[random.randrange(256) for i in range(n)]
    ts.sort()
    for t in ts:
        tree2(t)

###########


jungle2(100)


####turtle.mainloop()
