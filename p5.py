"""
n!=n*(n-1)*(n-2)*..*3*2*1
n-1!=(n-1)*(n-2)*..*3*2*1
n!=n*(n-1)!

"""
import matplotlib.pyplot as plt
def factorial(n):
    if not n:
        return 1
    else:
        return n*factorial(n-1)

def powR(a,b):
    if not b:
        return 1
    else:
##        return mul(a,powR(a,b-1))
        return a*powR(a,b-1)

def mul(a,b):
    if not b:
        return 0
    else:
##        return add(a,mul(a,b-1))
        return a+mul(a,b-1)

def inc(x):
    return x+1
def dec(x):
    return x-1

def add(a,b):
    if not b:
        return a
    else:
        return add(inc(a),dec(b))


def fib(n):
    """1 1 2 3 5 8 13 21 34 55"""
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fibo(n):
    if n==1 or n==2:
        return 1
    f=[1,1]
    for i in range(3,n+1):
        f.append(sum(f[-2:]))
##    f=[1 if i<=2 else f[i-2]+f[i-1]  for i in range(1,n+1)]    
##    print(f)
    return f[-1]

def neper(x,n):
    if not n:
        return 1
    else:
        return x**n/factorial(n) +neper(x,n-1)
def sin(x,n=10):
    r=0
    for i in range(n+1):
        temp=2*i+1
        r+= (-1)**i * x**temp/factorial(temp)
    return r

def cos(x,n=10):
    r=0
    for i in range(n+1):
        temp=2*i
        r+= (-1)**i * x**temp/factorial(temp)
    return r

def deg2rad(deg):
    import math
    return math.pi*deg/180
def draw_fib(n):
    x=[]
    x=[i for i in range(1,n+1)]
    y=[]
    y=[fibo(i) for i in x]
##    plt.plot(x,y,"rD")

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    line, = ax.plot(x,y,"rD")

    ax.set_yscale('symlog')

    
    plt.show()
    

def main():
    import math
    x=[]
    x=[i for i in range(0,361,10)]
    y=[]
    y=[sin(deg2rad(i)) for i in x]
    z=[cos(deg2rad(i)) for i in x]
    plt.plot(x,y)
    plt.plot(x,z,'cD')
    plt.show()

if __name__=="__main__":
    n=int(input("n = "))
    draw_fib(n)
##    main()




        
