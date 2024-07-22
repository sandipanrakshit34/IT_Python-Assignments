def fibo(n=1,a=0,b=1):
    if n>0:
        print(a)
        fibo(n-1,b,a+b)
n=int(input("Enter the terms: "))
fibo(n)