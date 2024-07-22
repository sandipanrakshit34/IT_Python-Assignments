L = [x for x in input("Enter words: ").split()]
L1=[item[::-1] for item in L]
L1.sort()
L1=[item[::-1] for item in L1]
print(L1)