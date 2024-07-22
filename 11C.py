def fibonacci(F3,n):
    a, b = 0, 1
    while a <= n:
        F3.write(str(a) + '\t')
        a, b = b, a + b

F3 = open('D:\My_CodePractice\Python_Practice\IT_Lab\FibonacciSeries.txt', 'w')
n = int(input("Enter the number of terms: "))
fibonacci(F3,n)
F3.close()