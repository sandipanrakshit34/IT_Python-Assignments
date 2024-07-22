def prime(n):
    for m in range(2,int(n**0.5)+1):
        if n % m ==0:
            break
        else:
            return n
prime = filter(prime, range(10500,251,-1))
print(list(prime))