#piramide
b=0;
for i in range(1,int(input())+1):
    #a = i;
    a = 0;
    b = i;
    while a<i:
        a+=1;
        print(a, sep='', end='')
    while b>1:
        b-=1;
        print(b,sep='',end='')
    print('\n')
