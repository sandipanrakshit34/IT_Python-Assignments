n = int(input("Enter the number of term: "))
print("The Fibonacci series is: ")
a,b= 0,1
for i in range(0,n+1):
    print(a,end=" ")
    a,b = b, a+b