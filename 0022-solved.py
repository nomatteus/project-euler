# Problem 22
# 19 July 2002

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.

# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938  53 = 49714.

# What is the total of all the name scores in the file?
import csv


def alpha_value(char):
    """
    Returns the alphabetical value for a character.
    i.e. A=1, C=3, Z26
    """
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char.upper()) + 1

assert 1 == alpha_value('a')
assert 3 == alpha_value('c')
assert 26 == alpha_value('Z')


def name_value(name):
    """
    Calculates and return name score value for a name
    """
    value = 0
    for char in name:
        value += alpha_value(char)
    return value

assert 54 == name_value('MATT')
assert 90 == name_value('MATTHEW')


def get_names():
    names = []
    with open('./0022-names.txt', 'r') as f:
        # names = f.read()
        reader = csv.reader(f)
        for row in reader:
            for col in row:
                names.append(col)
    return names


if __name__ == '__main__':
    names = get_names()
    names.sort()
    total_score = 0
    for i, name in enumerate(names):
        alph_list_position = i + 1
        score = alph_list_position * name_value(name)
        total_score += score
    print "The answer is %s" % total_score
