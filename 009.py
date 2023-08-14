# PROBLEM
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000 Find the product abc.

# PSEUDO
#
# Brute for with a double nested loop,
# increase value of a, b, c, checking if they add up t0 1000 first,
# then check if they are a pythagorean triple

def pythagorean_triple():
    target_sum = 1000
    # starting values to iterate from
    a = 10

    for i in range(500):
        a += 1
        b = a
        # carefully reset b after every set of iterations
        for j in range(500):
            b += 1
            c = b
            # carefully reset c after every set of iterations
            for k in range(500):
                c += 1
                # must add to 1000, and be a pythagorean triple to pass.
                if (a + b + c) == target_sum and (a**2 + b**2) == c**2:
                    print(f'a: {a}, b: {b}, c: {c}')
                    return (a*b*c)
                else:
                    continue


print(pythagorean_triple())