def fibo(x,y):
    print(x,y);
    x += y;
    y += x;
    if x > 1000:
       exit();
    else:
        fibo(x,y)

fibo(1,1)
