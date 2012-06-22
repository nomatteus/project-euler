#http://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
# n --> n/2 (n is even)
# n --> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the
# following sequence:
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# My approach: brute force.
# calculate chains for all starting numbers under a million, and
#   keep track of the starting number with the max chain


def calculate_sequence(num):
    """
    Calculates a sequence based on the following rules:
        n --> n/2 (n is even)
        n --> 3n + 1 (n is odd)
    """
    # Start off sequence with starting number
    sequence = [num]

    # Python does not have a do-while loop construct, so this emulates one
    # It's apparently known as a "loop and a half"
    # http://stackoverflow.com/questions/1662161/is-there-a-do-until-in-python
    while True:
        next = next_number(num)
        sequence.append(next)
        num = next  # set current num to next
        if next == 1:
            break
    return sequence


def next_number(num):
    if num % 2 == 0:
        next = num / 2
    else:
        next = 3 * num + 1
    return next

# Tests for helper function
assert [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] == calculate_sequence(13)
assert [1, 4, 2, 1] == calculate_sequence(1)
assert [2, 1] == calculate_sequence(2)
assert [3, 10, 5, 16, 8, 4, 2, 1] == calculate_sequence(3)

max_sequence = []

for i in range(1, 1000000):
    current_sequence = calculate_sequence(i)
    if len(current_sequence) >= len(max_sequence):
        max_sequence = current_sequence

print "The number that produces the longest chain is %s" % max_sequence[0]
print "The sequence is: %s items long." % len(max_sequence)
