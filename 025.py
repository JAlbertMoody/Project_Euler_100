# PROBLEM
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# PSEUDO
#
# Generate fib sequence until the length of current fib term is 999,
# keep track of the index with a counter and return it.

def fib(nth_term):
    fib_1 = 1
    fib_2 = 2

    for i in range(2, nth_term - 1):
        cache = fib_2
        fib_2 = fib_2 + fib_1
        fib_1 = cache
        print(f'first = {fib_1}, second = {fib_2}')

    print(len(str(fib_2)))
    return fib_2

# print(fib(12))

def thousand_digits(num_digits):
    index = 2

    fib_1 = 1
    fib_2 = 2

    while len(str(fib_2)) < num_digits:
        cache = fib_2
        fib_2 = fib_2 + fib_1
        fib_1 = cache
        index += 1
        # print(f'first = {fib_1}, second = {fib_2}')

    print(str(fib_2)[0])

    return index + 1

print(thousand_digits(1000))




