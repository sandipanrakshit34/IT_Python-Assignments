x =int(input("Enter the range: "))
for i in range(x):
    print(" "*(x-(i+1)),end='')
    for j in range(i+1,0,-1):
        print(chr(64+j),end='')
    print()
