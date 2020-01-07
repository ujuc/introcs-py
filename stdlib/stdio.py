"""
stdio.py

``stdio`` 모듈은 표준 입력으로부터 읽어오는 것과
``sys.stdout``으로 쓰는 것을 지원한다.

주의: 다음에 명시된 함수 묶음은 혼합하여 사용하지 않는다.

- ``is_empty()``, ``read_int()``, ``read_float()``, ``read_bool()``,
    ``read_string``
- ``has_next_line()``, ``read_line()``
- ``read_all()``, ``read_all_ints()``, ``read_all_floats()``,
    ``read_all_bools()``, ``read_all_strings()``, ``read_all_lines()``

하나 묶음만 사용하도록 한다.
"""

import sys
import re
import typing

sys.stdin = open(sys.stdin.fileno(), "r", newline=None)


# Writing functions


def writeln(x: str = "") -> None:
    """표준 출력으로 x를 쓰고 EOL(end-of-line)를 표시한다."""
    x = str(x)

    sys.stdout.write(x)
    sys.stdout.write("\n")
    sys.stdout.flush()


def write(x: str = "") -> None:
    """표준 출력을 x를 쓴다."""
    x = str(x)

    sys.stdout.write(x)
    sys.stdout.flush()


def writef(fmt: str, *args):
    """표준 출력으로 입력받은 format에 맞게 쓴다."""
    x = fmt % args

    sys.stdout.write(x)
    sys.stdout.flush()


# Reading functions

_buffer = ""


def _read_reg_exp(reg_exp: str) -> str:
    """
    표준 입력에서 앞에오는 공백을 삭제합니다.

    그런 다음 표준 출력에서 읽고 정규식 ``regExp``와 일치하는
    문자열을 반환합니다. 공백이 아닌 문자가 표준 입력
    버퍼에 남아있지 않으면 ``EOFError``을 발생합니다.
    표준 입력에서 읽을 문자가 ``regExp``와 일치하지 않으면
    ``ValueError``을 발생합니다.
    """
    global _buffer

    if is_empty():
        raise EOFError

    complied_reg_exp = re.compile(r"^\s*" + reg_exp)
    match = complied_reg_exp.search(_buffer)
    if match is None:
        raise ValueError

    s = match.group()
    _buffer = _buffer[match.end():]

    return s.lstrip()


def is_empty() -> bool:
    """
    표준 입력에 공백만 남아있다면 ``True``를 반환합니다.
    그렇지 않으면 ``False``.
    """
    global _buffer

    while _buffer.strip() == "":
        line = sys.stdin.readline()
        if line == "":
            return True
        _buffer += line

    return False


def read_int() -> int:
    s = _read_reg_exp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
    radix = 10
    str_length = len(s)

    if (str_length >= 1) and (s[0:1] == '0'):
        radix = 8
    if (str_length >= 2) and (s[0:2] == '-0'):
        radix = 8
    if (str_length >= 2) and (s[0:2] == '0x'):
        radix = 16
    if (str_length >= 2) and (s[0:2] == '0X'):
        radix = 16
    if (str_length >= 3) and (s[0:3] == '-0x'):
        radix = 16
    if (str_length >= 3) and (s[0:3] == '-0X'):
        radix = 16

    return int(s, radix)


def read_all_ints() -> typing.List[int]:
    strings = read_all_strings()

    return [int(s) for s in strings]


def read_float() -> float:
    s = _read_reg_exp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')

    return float(s)


def read_all_floats() -> typing.List[float]:
    strings = read_all_strings()

    return [float(s) for s in strings]


def read_bool() -> bool:
    s = _read_reg_exp(r'(True)|(False)|1|0')
    if (s == 'True') or (s == '1'):
        return True

    return False


def read_all_bools() -> typing.List[bool]:
    strings = read_all_strings()

    return [bool(s) for s in strings]


def read_string() -> str:
    s = _read_reg_exp(r'\S+')

    return s


def read_all_strings() -> typing.List[str]:
    strings = []
    while not is_empty():
        s = read_string()
        strings.append(s)

    return strings


def has_next_line() -> bool:
    global _buffer

    if _buffer != '':
        return True

    _buffer = sys.stdin.readline()

    if _buffer == '':
        return False

    return True


def read_line() -> str:
    global _buffer

    if not has_next_line():
        raise EOFError

    s = _buffer
    _buffer = ''

    return s.rstrip('\n')


def read_all_lines() -> typing.List[str]:
    lines = []

    while has_next_line():
        line = read_line()
        lines.append(line)

    return lines


def read_all() -> str:
    global _buffer

    s = _buffer
    _buffer = ''
    for line in sys.stdin:
        s += line

    return s
