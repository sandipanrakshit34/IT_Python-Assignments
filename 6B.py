l = []
n = int(input("Enter number of terms: "))
for i in range(n):
    t = int(input("Enter a integer: "))
    l.append(t)
print(l)
x = max(l)
l1 = [0]*(x+1)
for i in l:
    l1[i] = i
print(l1)