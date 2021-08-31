import threading
import time
import os
def print_odd(n):
    time.sleep(10)
    print("odd:",threading.current_thread().name, os.getpid())

def print_even(n):
    time.sleep(20)
    print("even:",threading.current_thread().name, os.getpid())
def print_odd1(n):
    time.sleep(10)
    print("odd:",threading.current_thread().name, os.getpid())

def print_even1(n):
    time.sleep(20)
    print("even:",threading.current_thread().name, os.getpid())

def print_odd_(n):
    time.sleep(10)
    print("odd:",threading.current_thread().name, os.getpid())

def print_even_(n):
    time.sleep(20)
    print("even:",threading.current_thread().name, os.getpid())
def print_odd1_(n):
    time.sleep(10)
    print("odd:",threading.current_thread().name, os.getpid())

def print_even1_(n):
    time.sleep(20)
    print("even:",threading.current_thread().name, os.getpid())



if __name__=="__main__":
    print("main:",threading.current_thread().name, os.getpid())
    t1=threading.Thread(target=print_odd,args=(100,),name='naxodd')
    t2=threading.Thread(target=print_even,args=(100,),name='naxeven')
    t3=threading.Thread(target=print_odd1,args=(100,),name='naxodd')
    t4=threading.Thread(target=print_even1,args=(100,),name='naxeven')
    t11=threading.Thread(target=print_odd_,args=(100,),name='naxodd')
    t22=threading.Thread(target=print_even_,args=(100,),name='naxeven')
    t33=threading.Thread(target=print_odd1_,args=(100,),name='naxodd')
    t44=threading.Thread(target=print_even1_,args=(100,),name='naxeven')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t11.start()
    t22.start()
    t33.start()
    t44.start()
##    t1.join()
##    t2.join()
    print("Good bye")























##import threading
##import time
##def print_odd(n):
##    time.sleep(20)
##    print("odd has been done")
##
##def print_even(n):
##    time.sleep(10)
##    print("even has been done")
##
##if __name__=="__main__":
##    t1=threading.Thread(target=print_odd,args=(100,))
##    t2=threading.Thread(target=print_even,args=(100,))
##    t1.start()
##    t2.start()
####    t1.join()
####    t2.join()
##    print("Good bye")



















##import threading
##
##def print_odd(n):
##    for i in range(1,n+1,2):
##        print(i)
##
##def print_even(n):
##    for i in range(0,n+1,2):
##        print(i)
##
##if __name__=="__main__":
##    t1=threading.Thread(target=print_odd,args=(100,))
##    t2=threading.Thread(target=print_even,args=(100,))
##    t1.start()
##    t2.start()
####    t1.join()
####    t2.join()
##    print("Good bye")
























##def path(n,m,way):
##    if n==0 and m==0:
##        print(way)
##        return
##    if n:
##        way1=way[:]
##        way1+="^"
##        path(n-1,m,way1)
##    if m:
##        way2=way[:]
##        way2+=">"
##        path(n,m-1,way2)
##if __name__=="__main__":
##    path(3,2,"")
##    
##








##def tm(n,m):
##	import random
##	l=[]
##	for i in range(m):
##		l.append(0)
##	for i in range(n):
##		c=random.randrange(0,m+n)
##		l.insert(c,1)
##	return l
##def am(n,m):
##	ls=[]
##	a=fac(n+m)/(fac(m)*fac(n))
##	while len(ls)!=a:
##		l=tm(n,m)
##		k=0
##		for i in ls:
##			if i==l:
##				k+=1
##		if k==0:
##			ls.append(l)
##	return ls
##def fac(a):
##	for i in range(1,a):
##		a*=i
##	return a
##if __name__=='__main__':
##	a=int(input())
##	b=int(input())
##	c=am(a,b)
##	d=1
##	for i in c:
##		print(d,end=' ')
##		for j in i:
##			print(j,end=' ')
##		print()
##		d+=1


##import turtle
##turtle.bgcolor('black')
##def drawshape(turtle,r):
##    turtle.circle(r,extent=60)
##    turtle.lt(120)
##    turtle.circle(r,extent=60)
##    
##def drawflower():
##    p=turtle.Turtle()
##    p.color('magenta')
##    p.speed(0)
##    p.pensize(4)
##    no_of_p=15
##    r=300
##    for i in range(no_of_p):
##        drawshape(p,r)
##        p.lt(360/no_of_p)
##
##drawflower()




#turtle.done()

##import turtle
##import random
##pen= turtle.Turtle()
##
##pen.speed(0)
##turtle.bgcolor("#2d3436")
##
##
##def screensaver(i,count):
##    count=count
##    n=i
##    colors=["#fdcb6e","#d63031","#fd79a8",'#74b9ff','#55efc4']
##    pensize=0.5
##    size=10
##    for i in range(count):
##        polygon(n,colors[i%5],size,pensize)
##        pensize+=.25
##        size+=5
##    pen.clear()
##
##def polygon(n, color='greenyellow',size=100,pensize=5):
##    pen.color(color)
##    pen.pensize(pensize)
##    angle = 360/n
##    for i in range(n):
##        pen.lt(angle)
##        for i in range(n):
##            pen.fd(size)
##            pen.lt(angle)
##
##
##
##def run_screensaver(n,m,count):
##    for i in range(n,m+1):
##        screensaver(i,count)
##
##
##
##polygon(20)
##
####run_screensaver(4,10,10)
