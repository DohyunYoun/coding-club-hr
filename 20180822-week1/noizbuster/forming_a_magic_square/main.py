#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

def getSums(flatten, balance):
    sums = [
        flatten[0] + flatten[3] + flatten[6] - balance,
        flatten[1] + flatten[4] + flatten[7] - balance,
        flatten[2] + flatten[5] + flatten[8] - balance,
        flatten[0] + flatten[1] + flatten[2] - balance,
        flatten[3] + flatten[4] + flatten[5] - balance,
        flatten[6] + flatten[7] + flatten[8] - balance
    ]
    return sums

def classify(iset):
    negative = 0
    positive = 0
    for item in iset:
        if item > 0:
            positive += item
        else:
            negative += item
    return {'positive': positive, 'negative': negative}

# remove value from items of targetSet
def interpolate(value, targetSet):
    remains = value;
    for item in targetSet:
        if item * remains > 0 and item < remains:
            item = 0
            remains -= item
    return {'targetSet': targetSet, remains: }

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    print(s)
    flatten = reduce(lambda x,y: x + y, s)
    print('flatten input', flatten)
    sums = getSums(flatten, 0)
    print('sums', sums)
    mean = reduce(lambda x, y: (x + y) / 2, sums)# / len(s)
    mean = round(mean)
    print('mean is ', mean)
    # balance = round(mean * 3)
    # print('mean of one line is', balance)
    
    optimal = sys.maxsize
    # search optimal
    for i in range(mean, 28):
        su = getSums(flatten, i)
        l = su[:3]
        r = su[3:]
        print(i, su, l, r)
        print(classify(l), classify(r))
        # score_l = reduce(lambda x, y: (abs(x) + abs(y)) , l)# / len(s)
        # score_r = reduce(lambda x, y: (abs(x) + abs(y)) , r)# / len(s)
        # if optimal > max(score_l, score_r):
        #     optimal = max(score_l, score_r)

    # diffSum = reduce(lambda x, y: (x + abs(y)) , sums)# / len(s)
    # print('diffSum is', diffSum)
    return optimal

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []
    # i = ['4 9 2','3 5 7','8 1 5']
    i = ['4 8 2', '4 5 7', '6 1 6']

    for _ in range(3):
        s.append(list(map(int, i[_].rstrip().split())))
    print('s is',s)
    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print('result:', result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
