"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError("Number of primes is 0 or negative")

    list.append(2)

    i = 3
    while len(list) < number_of_primes:
        isPrime = True
        for j in range(i-1,1,-1):
            if i % j == 0:       #If it is divisible by a number less than it, or a number down to 2, then it is not prime
                isPrime = False
                break
        
        if isPrime:
            list.append(i)
            
        i = i+1    

    return list

print(primes(5))