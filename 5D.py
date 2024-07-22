str  = input('Enter a string , start index, end index: ')
l1 = str.split()
ep = int(l1[-1])
sp = int(l1[-2])
l1 = l1[:len(l1)-2]
str = " ".join(l1)
# print(str)
substr = str[sp-1:ep]
if substr == substr[::-1]:
    print(substr,"palindrome")
else:
    print(substr,"not palindrome")