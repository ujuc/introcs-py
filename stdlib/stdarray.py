"""
stdarray.py

``stdarray`` 모듈은 1차원과 2차원 배열의 생성, 읽기, 쓰기에 관련된 기능을 정의한다.
"""

import stdlib.stdio as stdio


def create_1d(length, value=None):
    return [value] * length


def create_2d(row_count, col_count, value=None):
    a = [None] * row_count

    for row in range(row_count):
        a[row] = [value] * col_count

    return a


def write_1d(a):
    length = len(a)
    stdio.writeln(length)

    for i in range(length):
        element = a[i]
        if isinstance(element, bool):
            if element == True:
                stdio.write(1)
            else:
                stdio.write(0)
        else:
            stdio.write(element)

        stdio.write(' ')

    stdio.writeln()


def write_2d(a):
    row_count = len(a)
    col_count = len(a[0])
    stdio.writeln(str(row_count) + ' ' + str(col_count))

    for row in range(row_count):
        for col in range(col_count):
            element = a[row][col]
            if isinstance(element, bool):
                if element == True:
                    stdio.write(1)
                else:
                    stdio.write(0)
            else:
                stdio.write(element)

            stdio.write(' ')

        stdio.writeln()


def read_int_1d():
    count = stdio.read_int()
    a = create_1d(count, None)
    for i in range(count):
        a[i] = stdio.read_int()

    return a


def read_int_2d():
    row_count = stdio.read_int()
    col_count = stdio.read_int()
    a = create_2d(row_count, col_count, 0)

    for row in range(row_count):
        for col in range(col_count):
            a[row][col] = stdio.read_int()

    return a


def read_float_1d():
    count = stdio.read_int()
    a = create_1d(count, None)

    for i in range(count):
        a[i] = stdio.read_float()

    return a


def read_float_2d():
    row_count = stdio.read_int()
    col_count = stdio.read_int()
    a = create_2d(row_count, col_count, 0.0)

    for row in range(row_count):
        for col in range(col_count):
            a[row][col] = stdio.read_float()

    return a


def read_bool_1d():
    count = stdio.read_int()
    a = create_1d(count, None)

    for i in range(count):
        a[i] = stdio.read_bool()

    return a


def read_bool_2d():
    row_count = stdio.read_int()
    col_count = stdio.read_int()
    a = create_2d(row_count, col_count, False)

    for row in range(row_count):
        for col in range(col_count):
            a[row][col] = stdio.read_bool()

    return a
