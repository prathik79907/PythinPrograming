n=int(input("enter the no.of series:"))
a=0
b=1
while(n>0):
    c=a+b
    print(a)
    a=b
    b=c
    n=n-1
