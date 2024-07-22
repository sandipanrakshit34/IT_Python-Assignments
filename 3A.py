a = eval(input("Enter the first number: "))
b = eval(input("Enter the second number: "))
c = eval(input("Enter the third number: "))
if b <= a >= c:
    print("the maximum number is: ",a)
elif a <= b >= c:
    print("the maximum number is: ",b)
elif a <= c >= b:
    print("the maximum number is: ",c)

# max_number = max(a, b, c)

# print("The maximum number is:", max_number)
