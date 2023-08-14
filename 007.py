# PROBLEM
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# What is the 10,001st prime number?

# PSEUDO
#
# generate prime number for 10,001 iterations
# every prime must be added to a list to check if the next one is prime
# a prime number cannot be divisible by other primes, that how we check
#

def find_nth_prime(n):
    primes = [2]
    num = 2
    # iterate up to the nth prime
    while len(primes) < n:
        num += 1
        is_prime = True
        # Assume num is prime until proven otherwise

        # Check if num is divisible by any prime
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                # num is not prime
                break

        if is_prime:
            primes.append(num)

    return primes[-1]

print(find_nth_prime(10_001))





















