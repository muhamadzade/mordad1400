def honoi(n,a,b,c):
    if n:
        honoi(n-1,a,c,b)
        print(f"{n}:{a}->{c}")
        honoi(n-1,b,a,c)


honoi(10,'A','B','C')
