# PROBLEM
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600,851,475,143?

# PSEUDO
#
#  divide our way up the primes
#  generate a new prime number if needed at every iteration
#  divide by 2 while num % 2 == 0, every time that's true, add to prime factor list
#  when false try next prime, in this case 3, while num % 3 ==0
#  process is finished when num = 1
#  retrun max value of factors list

def prime_factor(num):
    factors = []
    primes = [2]
    prime = 2
    while num > 1 and prime < 700_000_000_000:
        # added a prime max just for preventing infinite looping
        # if num == 1, then it is factored out
        if prime > num:
            # if the current prime is greater than the current num,
            # that is the last factor. loop is done
            factors.append(int(num))
            break
        elif num % prime == 0:
            factors.append(prime)
            num = num / prime
            continue
        #     if the current prime factors the num, add it to the list, and try again.
        else:
            # define a variable as true to control loop
            search_for_prime = True
            while search_for_prime:
                prime +=1
                # add one to current prime and check if it is divisible by
                # any past primes
                for i in range(len(primes)):
                    if prime % primes[i] == 0:
                        # if it's divisible by any primes, keep iterating and searching
                        continue
                    else:
                        # it is a prime, exit the inner loop and outer loop.
                        # print(f'prime found: {prime}')
                        primes.append(prime)
                        search_for_prime = False
                        break

    return(factors)

print(prime_factor(600851475143))


