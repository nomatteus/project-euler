# Problem 35
# 17 January 2003
# http://projecteuler.net/problem=35

# The number, 197, is called a circular prime because all rotations of the
#   digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
#   71, 73, 79, and 97.

# How many circular primes are there below one million?

import math


# Taken from 0007 solution
def is_prime(n):
    max_check = math.sqrt(n)
    if n == 1:
        return False
    for i in range(2, int(max_check) + 1):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    n = str(n)
    num_digits = len(n)
    for i in range(0, num_digits):
        # Move i digits from front to back of n
        # n[:2] is first i digits, n[2:] is everything but the first i digits
        flipped = n[i:] + n[:i]
        if not is_prime(int(flipped)):
            return False
    return True

assert is_circular_prime(197)
assert not is_circular_prime(198)


def circular_primes_below(n):
    circular_primes = []
    for i in range(1, n):
        # These checks are quick and dirty, but reduced runtime from 16s to 8s
        if not(i != 2 and i % 2 == 0) and \
          not(i != 3 and i % 3 == 0) and \
          not(i != 5 and i % 5 == 0) and \
          not(i != 7 and i % 7 == 0) and \
          not(i != 11 and i % 11 == 0) and \
          not(i != 13 and i % 13 == 0) and \
          is_circular_prime(i):
            circular_primes.append(i)
    return circular_primes

assert [] == circular_primes_below(2)
assert [2] == circular_primes_below(3)
assert [2, 3, 5] == circular_primes_below(6)
assert [2, 3, 5, 7, 11, 13, 17, 31, 37] == circular_primes_below(50)
assert 13 == len(circular_primes_below(100))


def solve35():
    circular_primes = circular_primes_below(1000000)
    return len(circular_primes)

answer = solve35()

print "the answer is %s" % answer
