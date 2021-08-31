def p_set(n,s):
    global count
    if n==0:
        print(count,s)
        count+=1
    else:
        p_set(n-1,s)
        p_set(n-1,s|{n})

def power_set(n):
    s=set()
    p_set(n,s)

def bin2set(x):
    b=x
    b=b[::-1]
    b=b[:-2]
##    print(b)
    s=set()
    for i,j in enumerate(b):
        if j=='1':
##            print('j',i)
            s|={i+1}
    print(s)
        

def p_set2(n):
    for i in range(2**n):
        x=bin(i)
        print(x,end='')
        bin2set(x)

if __name__=="__main__":
##   count=0
##    bin2set(bin(5))
   p_set2(5) 
























##def square(n,symbole='*'):
##    for i in range(1,n+1):
##        print(f"{symbole} "*n)
##
##def rect(n=1,m=1):
##    for i in range(1,n+1):
##        print("* "*m)
##
##def triangle(n):
##    for i in range(1,n+1):
##        print("* "*i)
##
##def triangle_reverse(n):
##    for i in range(n,0,-1):
##        print("* "*i)
##
##def mountain(n):
##    triangle_complete(n)
##        
##def triangle_complete(n):
##    triangle(n)
##    triangle_reverse(n-1)
##
##def hill(n,m):
##    triangle(n-1)
##    rect(m,n)
##    triangle_reverse(n-1)
##    
##def zamin(n=100):
##    import random
##    for i in range(n):
##        if random.random()<.7:
##            h=random.randrange(2,10)
##            mountain(h)
##        else:
##            h=random.randrange(2,10)
##            w=random.randrange(3,6)
##            hill(h,w)
##
##"""
##n=7
##        space       *
##    *
##   * * 
##  *   *
## *     *
##*       *
## *     *
##  *   *
##   * * 
##    *
##"""
##def diamondB(n):
##    print("  "*(n//2)+'*')    
##    for i in range(3,n+1,2):
##        print("  "*((n-i)//2)+"* "+"  "*(i-2)+"* ")
##    for i in range(n-2,2,-2):
##        print("  "*((n-i)//2)+"* "+"  "*(i-2)+"* ")
##
##    print("  "*(n//2)+'*')    
##
##
##
##
##"""
##n=7
##        space       *
##   *     3          1
##  ***    2          3
## *****   1          5 
##*******  0=(n-i)/2  7
## *****   1          5
##  ***    2          
##   *
##"""
##def triangleU(n):
##    for i in range(1,n+1,2):
##        print("  "*((n-i)//2)+"* "*i)
##
##def triangleD(n):
##    for i in range(n-2,0,-2):
##        print("  "*((n-i)//2)+"* "*i)
##
##    
##def diamond(n):
##    triangleU(n)
##    triangleD(n)
##
##if __name__=="__main__":
##    diamondB(9)
####    for i in range(1,21,2):
####        diamond(i)
##
##    
####    zamin(10)
####    square(5,"#")



























##def swap(a,b):
##    a,b=b,a
##    print(a,b)
##def swap2():
##    global x
##    global y
##    x,y=y,x
##def swap3(ls):
##    ls[0], ls[1]=ls[1], ls[0]
##
##if __name__=="__main__":
##    x=3
##    y=4
##    ls=[x,y]
##    print(ls)
##    swap3(ls)
##    print(ls)
    























##def person(**args):
##    s1=f"I am {args['fname']} {args['lname']}."
##    s2=f"I am from {args['city']}."
##    age=2021-args['year']
##    s3=f"I am {age} years old."
##    print(s1+"\n"+s2+"\n"+s3)
##
##
##if __name__=="__main__":
##    person(fname="Ali",
##           lname='Alavi',
##           city= 'Tehran',
##           year= 2000)
##    person("naqi",'mamoli')

























##def person(*args):
##    s1=f"I am {args[0]} {args[1]}."
##    s2=''
##    if len(args)>2:
##        s2=f"I am from {args[2]}."
##    s3=''
##    if len(args)>3:
##        age=2021-args[3]
##        s3=f"I am {age} years old."
##    print(s1+"\n"+s2+"\n"+s3)
##
##
##if __name__=="__main__":
##    person("Ali",'Alavi','Tehran',2000)
##    person("naqi",'mamoli')
##    person('Naqi')
##    person(city='Tehran',
##           fname='Homa',
##           year=1985,
##           lname='sadat')























##def person(fname,
##           lname='Mamoli',
##           city='Aliabad',
##           year=1990):
##    s1=f"I am {fname} {lname}."
##    s2=f"I am from {city}."
##    age=2021-year
##    s3=f"I am {age} years old."
##    print(s1+"\n"+s2+"\n"+s3)
##
##
##if __name__=="__main__":
##    person("Ali",'Alavi','Tehran')
##    person('Naqi')
##    person(city='Tehran',
##           fname='Homa',
##           year=1985,
##           lname='sadat')























##def print_hello():
##    print('salam')
##    print_bye()
##
##def print_bye():
##    print('خداحافط رفيق')
####    print_hello()
##
####print_hello()
##
##if __name__=="__main__":
##    print_hello()
##else:
##    print("Welcome to p4 module, the best module in the world.")
##


    

##def esm_tabe(vorodiha):
##    badaneye_tabe
##    badaneye_tabe
##badaneye_tabe_kharej_ast


    
