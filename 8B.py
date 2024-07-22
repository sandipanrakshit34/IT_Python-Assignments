import numpy as np
A = []
r = int(input('Enter number of Rows: '))
c = int(input('Enter number of Columns: '))
print('Enter',r*c,'Elements: ')
for i in range(r):
    row = []
    for j in range(r):
        row.append(int(input()))
    A.append(row)
print('A= ')
print(A)
arr = np.random.randint(1,20,r*c)
B = arr.reshape(c, r)
print('B= ')
print(B)
C = np.dot(A,B)
print('C= ')
print(C)