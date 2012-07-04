# Problem 7
# 28 December 2001
# http://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#   we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# First solution (July 4, 2012, 320pm): 44 seconds to run
# Second solution (July 4, 330pm): under 1 second
#         (by changing max to check from n/2 to sqrt(n))

import math


def is_prime(n):
    """
    Determine whether a number is prime or not
    Returns boolean.
    Searches from 2 to n/2 and tests for divisibility. As soon as a divisor
    is found, False is returned. If n makes it through the divisibility
    gauntlet (no divisors found), return True.
    """
    max_check = math.sqrt(n)
    for i in range(2, int(max_check) + 1):
        if n % i == 0:
            return False
    return True

assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(5)
assert not is_prime(6)
assert is_prime(7)
assert not is_prime(8)
assert not is_prime(9)
assert not is_prime(10)
assert is_prime(11)
assert not is_prime(12)
assert is_prime(13)


def get_nth_prime(n):
    """
    This loops through all numbers starting from 2, and generates a list
    of primes until we have n primes. Quite inefficient. One optimization
    would be to store the list of primes so it's not regenerated each time
    and only regenerate more if n is larger than all other n's that have been
    requested.
    """
    primes = []
    num = 2  # starting point
    # "do-while" emulation in Python
    # http://stackoverflow.com/questions/1662161/is-there-a-do-until-in-python
    while True:
        if (is_prime(num)):
            primes.append(num)
        if len(primes) == n:
            return primes[-1]
        num += 1

assert 2 == get_nth_prime(1)
assert 3 == get_nth_prime(2)
assert 5 == get_nth_prime(3)
assert 7 == get_nth_prime(4)
assert 11 == get_nth_prime(5)
assert 13 == get_nth_prime(6)
assert 7919 == get_nth_prime(1000)

answer = get_nth_prime(10001)
print "the answer is %s" % answer

# Now that I've solved it, assert the answer to assure correct refactoring
assert 104743 == answer
