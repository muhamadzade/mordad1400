import turtle as t
from threaded_turtle import ThreadSerializer, TurtleThread

crt=ThreadSerializer()
t1=t.Turtle()
t2=t.Turtle()
def ft(t1):
    t1.speed(0)
    i=0
    for i in range(360):
        t1.forward(i)
        t1.lt(1)
def st(t2):
    t2.speed(0)
    i=0
    for i in range(360):
        t2.forward(i)
        t2.lt(1)
if __name__=='__main__':
    tf=TurtleTread(crt, t1, target=ft)
    sf=TurtleTread(crt, t2, target=st)
    tf.daemon=True
    tf.start()
    sf.daemon=True
    sf.start()
    crt.run_forever(1)

