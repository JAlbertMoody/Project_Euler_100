# PROBLEM
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# PSEUDO
#
# create a list of "True" bools with a length of "limit". index corresponds to the number
# loop through the numbers and once an abundant number is found, mark it as false
# after looping, loop again and find all the combinations of two and mark as false
# finally loop again and fin the sum af all the non abundant numbers

def non_abundant_sums(limit):
    # initiate the list and set its length
    is_abundant = [False] * limit

    # first loop to mark abundant numbers
    for num in range(1, limit):
        if not is_abundant[num]:
        # find and sum the factors to test abundance
            factors = []
            for i in range(1, num//2 + 1):
                if num % i == 0:
                    factors.append(i)
            # if it is abundant, mark it as abundant
            if sum(factors) > num:
                # print(sum(factors), num)
                is_abundant[num] = True
    # print(is_abundant)

    #initiate a list to find sums of two abundant nums
    is_abundant_sum = [False] * limit

    for index, bool in enumerate(is_abundant):
        if bool and index*2 < limit:
            is_abundant_sum[index*2] = True
            for i in range(index, limit):
                if is_abundant[i] and index + i < limit:
                    is_abundant_sum[index + i] = True
    # print(is_abundant_sum)

    # return the sum of all the non_abundant sum numbers
    return sum(index for index, bool in enumerate(is_abundant_sum) if not bool)


print(non_abundant_sums(28124))