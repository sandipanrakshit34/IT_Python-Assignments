print("All two digits automorphic numbers are: ")
for i in range(10,100):
    if((i**2)%100 == i):
        print(i)