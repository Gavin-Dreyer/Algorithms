#!/usr/bin/python

import sys

# all possible plays which when given n number of plays
# create a list equal to n^3
# start with rock


def rock_paper_scissors(n):
    options = [['rock'], ['paper'], ['scissors']]
    results = []
    index = 0
    index2 = 0
    count = 0
    count2 = 0
    count3 = 0

    if n == 0:
        return [[]]
    elif n == 1:
        return options
    else:
        def recurse_create(opt, arr, n):
            if len(arr) == 3**n:
                def recurse_populate(opt, arr, n):
                    if n < 2:
                        return arr

                    nonlocal count2, index2, count3
                    index2 = 0
                    count2 = 0
                    count3 = 0
                    while True:
                        if count2 == (3**(n - 2)):
                            count2 = 0
                            index2 += 1
                        elif index2 == 3:
                            index2 = 0
                        elif count3 == len(arr):
                            break
                        else:
                            arr[count3] = arr[count3] + opt[index2]
                            count2 += 1
                            count3 += 1

                    return recurse_populate(opt, arr, n - 1)
                return recurse_populate(opt, arr, n)
            else:
                nonlocal count, index
                for i in range(3):
                    if count == 3**(n-1):
                        count = 0
                        index += 1
                    elif index == 3:
                        index = 0
                    else:
                        arr = arr + [opt[index]]
                        count += 1
            return recurse_create(opt, arr, n)
        return recurse_create(options, results, n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
