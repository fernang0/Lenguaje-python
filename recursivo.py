def recursive(n,r):
    print(n,"x",r,"=",n*r);
    if r < 10:
        r+=1;
        recursive(n,r);

factor = int(input("Ingresa la tabla de multiplicar que desea saber: "));
recursive(factor,1);


