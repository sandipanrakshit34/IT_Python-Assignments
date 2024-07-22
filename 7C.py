def gcdlcm(a,b=1):
    x,y=a,b
    if(a<b):
        a,b=b,a
    while a%b!=0:
        a,b=b,a%b
    lcm=(x*y)//b
    return b,lcm
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
g,l=gcdlcm(a,b)
print(gcdlcm(a,b))