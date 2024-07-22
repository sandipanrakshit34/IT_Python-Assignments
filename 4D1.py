x = int(input("Enter the number of rows: "))
l = x//2
for i in range(1,l+2):
    print(" "*(l+1-i),end='')
    print("*"*(2*i-1))
for i in range(l,0,-1):
    print(" "*(l+1-i),end='')
    print("*"*(2*i-1))