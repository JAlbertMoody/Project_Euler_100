# PROBLEM
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# PSEUDO
#
# Find all the primes below 2_000_000 and add them to a list
# sum the list and return the answer
# Lots of primes problems in this set.

def sum_primes():
    primes = [2]
    num = 2
    sum = 2

    # find all the primes below 2 million
    while num < 2000000:
        num += 1
        # assume True unless proven otherwise
        isPrime = True
        # test if any primes can divide num
        for prime in primes:
            if num % prime == 0:
                # Not a prime, set to false
                isPrime = False
                break
            else:
                continue
        if isPrime:
            # add to primes list
            primes.append(num)
            sum += num
            # print(primes)

    # print(primes)
    # return the summed list
    return sum

print(sum_primes())

# Very slow to execute, will consider using 'Sieve of Eratosthenes'


