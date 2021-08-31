
def op(f):
    def f1():
        print("Hello")
        f()
        print("Bye")
    return f1
    

@op
@op
def g():
    print("*"*10)

##g=op(g)

g()




##def f1():
##    def f2(name):
##        print(f"Hello {name}")
##    return f2
##
##
##f3=f1()
##f3("hasan")













##def inc(x):
##    return x+1
##def dec(x):
##    return x-1
##
##def op(f,a):
##    return f(a)
##
##print(op(dec,10))





##def print_hello(name):
##    print(f"Hello {name}")
##
##
##print2=print_hello
##print2("hasan")    











##import sys
##sys.path.append('C:/prg/mordad1400')
##import matplotlib.pyplot as plt
##from p5 import sin,deg2rad
##x=list(range(361))
##y=list(map(lambda a: sin(deg2rad(a)) , x))
##plt.plot(x,y)
##plt.show()





##f=lambda a:2*a
##g=lambda a,b:a**b
##h=lambda n: 1 if n==0 else n*h(n-1)
##
##
##print(h(5))
##
##
##
##















##import p5
##p5.main()
##print(p5.sin(p5.deg2rad(30)))
