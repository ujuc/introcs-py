"""
stdrandom.py

stdrandom 모듈은 모의 랜덤 숫자와 관련된 기능을 정의합니다.
"""

import math
import random


def seed(i=None):
    random.seed(i)


def uniform_int(lo, hi):
    return random.randrange(lo, hi)


def uniform_float(lo, hi):
    return random.randrange(lo, hi)


def bernoulli(p=0.5):
    return random.random() < p


def binomial(n, p=0.5):
    heads = 0
    for _ in range(n):
        if bernoulli(p):
            heads += 1

    return heads


def gaussian(mean=0.0, stddev=1.0):
    x = uniform_float(-1.0, 1.0)
    y = uniform_float(-1.0, 1.0)
    r = x * x + y * y

    while (r >= 1) or (r == 0):
        x = uniform_float(-1.0, 1.0)
        y = uniform_float(-1.0, 1.0)
        r = x * x + y * y

    g = x * math.sqrt(-2 * math.log(r) / r)

    return mean + stddev * g


def discrete(a):
    r = uniform_float(0.0, sum(a))
    subtotal = 0.0

    for i in range(len(a)):
        subtotal += a[i]
        if subtotal > r:
            return i


def shuffle(a):
    random.shuffle(a)


def exp(lambd):
    return -math.log(1 - random.random()) / lambd
