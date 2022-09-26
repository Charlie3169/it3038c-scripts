## Take a number input and calculate how many prime numbers come between it and 0

def piFunction(n):
    primeCount = 0       
    for i in range(2, n):
        if(isPrime(i)): 
            primeCount += 1
    return primeCount

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:            
            return False     
    return True

print("Pi Function Calculator!")
number = int(input("Please enter a number: "))
print("Number of primes less than or equal to that number: ", piFunction(number))