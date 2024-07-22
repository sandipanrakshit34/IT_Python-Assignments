str = input("Enter the sentence: ")
lc,uc=0,0
for i in range(0, len(str)):
    if str[i].isupper():
        uc+=1
    elif str[i].islower():
        lc+=1
print(uc,lc)