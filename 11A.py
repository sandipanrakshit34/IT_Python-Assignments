import os
F1 = open('D:\My_CodePractice\python\IT\Test171123.txt','w')
F1.write('Welcome to Python')
F1.close()

size = os.path.getsize('D:\My_CodePractice\python\IT\Test171123.txt')
print("Size of file is", size, "bytes")