def is_palindrome_number(num):
    # See extended slices:
    # http://docs.python.org/release/2.3.5/whatsnew/section-slices.html
    return str(num) == str(num)[::-1]

assert True == is_palindrome_number(1)
assert True == is_palindrome_number(12321)
assert True == is_palindrome_number(99999)
assert False == is_palindrome_number(33322)


def get_palindromes():
    palindromes = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindrome_number(i * j):
                palindromes.append((i * j, i, j))
    return palindromes

highest = max(get_palindromes())

print "Answer to problem 4 is: %s" % highest[0]
