def primeCheck(n):
    for i in range(2,n):
        if n%i == 0:
            break
        else:
            if n>1:
                return True
        return False
    
def palindromeCheck(n):
    sum = 0
    n1 = n 
    while n1 != 0:
        sum = sum*10 + n1%10
        n1 //= 10
    if sum == n:
        return True
    else:
        return False
    
# if __name__ == "__main__":
#     print("Hello World")
#     print(1,primeCheck(131))
#     print(2,palindromeCheck(313))

# print("Helllo World2")
# print(1,primeCheck(131))
# print(2,palindromeCheck(313))