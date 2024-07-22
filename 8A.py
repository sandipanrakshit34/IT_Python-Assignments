import numberCheck8A as nc

if __name__ == "__main__":
    n = int(input("Enter an integer number: "))

    pr = nc.primeCheck(n)
    pa = nc.palindromeCheck(n)

    if pr and pa:
        print(n,"is prime and palindrome")
    elif pr:
        print(n,"is prime but not palindrome")
    elif pa:
        print(n,"is not prime but palindrome")
    else:
        print(n,"is neither prime nor palindrome")