"""
picture.py

``picture`` 모듈은 Picture 클래스를 정의한다.
"""

import pygame

import stdlib.color as color


class Picture:
    """
    ``Picture`` 클래는 이미지를 모델링한다. 이미지는 주어진 폭, 높이와
    모든 블랙 픽셀을 포함합니다. 나중에 저장된 JPG이나 PNG 이미지를
    읽어올 수 있다.
    """

    def __init__(self, arg1=None, arg2=None):
        if (arg1 is None) and (arg2 is None):
            max_w = 512
            max_h = 512
            self._surface = pygame.Surface((max_w, max_h))
            self._surface.fill((0, 0, 0))
        elif (arg1 is not None) and (arg2 is None):
            file_name = arg1
            try:
                self._surface = pygame.image.load(file_name)
            except pygame.error:
                raise IOError()
        elif (arg1 is not None) and (arg2 is not None):
            max_w = arg1
            max_h = arg2
            self._surface = pygame.Surface((max_w, max_h))
            self._surface.fill((0, 0, 0))
        else:
            raise ValueError()

    def load(self, f):
        pass

    def save(self, f):
        pygame.image.save(self._surface, f)

    def width(self):
        return self._surface.get_width()

    def height(self):
        return self._surface.get_height()

    def get(self, x, y):
        pygame_color = self._surface.get_at((x, y))
        return color.Color(pygame_color.r, pygame_color.g, pygame_color.b)

    def set(self, x, y, c: color.Color):
        pygame_color = pygame.Color(c.get_rad(), c.get_green(), c.get_blue(), 0)
        self._surface.set_at((x, y), pygame_color)
