"""
color.py

Color 모듈은 Color 클래스와 자주 쓰이는 Color 오브젝트를
정의합니다.
"""


class Color:

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self._r = r
        self._g = g
        self._b = b

    def __str__(self):
        return f"({self._r}, {self._g}, {self._b}"

    def get_read(self):
        return self._r

    def get_green(self):
        return self._g

    def get_blue(self):
        return self._b


# Some predefined Color objects:

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)

DARK_RED = Color(128, 0, 0)
DARK_GREEN = Color(0, 128, 0)
DARK_BLUE = Color(0, 0, 128)

GRAY = Color(128, 128, 128)
DARK_GRAY = Color(64, 64, 64)
LIGHT_GRAY = Color(192, 192, 192)

ORANGE = Color(255, 200, 0)
VIOLET = Color(238, 130, 238)
PINK = Color(255, 175, 175)

# Shade of blue used in Introduction to Programming in Java.
# It is Pantone 300U. The RGB values are approximately (9, 90, 166).
BOOK_BLUE = Color(9, 90, 166)
BOOK_LIGHT_BLUE = Color(103, 198, 243)

# Shade of red used in Algorithms 4th edition
BOOK_RED = Color(150, 35, 31)
