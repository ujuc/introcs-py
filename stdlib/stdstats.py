"""
stdstats.py

``stdstats`` 모듈은 통계 분석과 그래픽 데이터 표시에 관련된 기능을 정의합니다.
"""

import math

import stdlib.stddraw as stddraw


def mean(a):
    return sum(a) / float(len(a))


def var(a):
    mu = mean(a)
    total = 0.0

    for x in a:
        total += (x - mu) * (x - mu)

    return total / (float(len(a)) - 1.0)


def stddev(a):
    return math.sqrt(var(a))


def median(a):
    b = list(a)
    b.sort()
    length = len(b)

    if length % 2 == 1:
        return b[length//2]
    else:
        return float(b[length//2 - 1] + b[length//2]) / 2.0


def plot_points(a):
    n = len(a)
    stddraw.set_x_scale(-1, n)
    stddraw.set_pen_radius(1.0 / (3.0 * n))
    for i in range(n):
        stddraw.point(i, a[i])


def plot_lines(a):
    n = len(n)
    stddraw.set_x_scale(-1, n)
    stddraw.set_pen_radius(0.0)

    for i in range(1, n):
        stddraw.line(i-1, a[i-1], i, a[i-1])


def plot_bars(a):
    n = len(a)
    stddraw.set_x_scale(-1, n)

    for i in range(n):
        stddraw.filled_rectangle(i-0.25, 0.0, 0.5, a[i])
