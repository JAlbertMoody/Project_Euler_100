# PROBLEM
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# PSEUDO
#
# Use the "Sieve of Eratosthenes" algorithm to find primes up to the limit.


def SOE_primes(limit):
    # initiate is prime as a list of 'True" bools, with a length of 'limit'
    is_prime = [True] * (limit)
    # set index 0 and 1 to False as they are not primes
    is_prime[0], is_prime[1] = False, False

    # only check to sqrt of limit, as that's the largest possible factor
    for num in range(2, int(limit**0.5)):
        if is_prime[num]:
            # mark all multiples of the known prime as not prime
            # so if num = 2, 4, 6, 8, ... will be marked as not prime and skipped next time.
            for multiple in range(num*num, limit, num):
                # mark the index at that multiple as not prime.
                is_prime[multiple] = False

    prime_sum = sum(num for num, prime in enumerate(is_prime) if prime)
    # print(is_prime)
    return prime_sum

limit = 2_000_000
print(SOE_primes(limit))

