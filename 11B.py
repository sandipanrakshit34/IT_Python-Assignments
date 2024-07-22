def prime(f2, n):
    i = 2
    count = 0
    while True:
        for j in range(2,i):
            if i%j == 0:
                i += 1
                break
        else:
            F2.write(str(i)+'\t')
            i += 1
            count += 1
        if count == n:
            break
F2 = open('D:\My_CodePractice\Python_Practice\IT_Lab\Prime.txt','w')
n = int(input('Enter number of terms: '))
prime(F2, n)
F2.close()
