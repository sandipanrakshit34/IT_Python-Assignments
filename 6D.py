l1 = input("Enter a string: ")
l2 = l1.split()
s1 = set(l2)
d = {}
for i in s1:
    d[i] = l2.count(i)
print(d)