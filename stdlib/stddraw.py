"""
stddraw.py

``stddraw`` 모듈은 화면을 그릴 수 있도록 도와주는 함수를
정의합니다. canvas에 나타냅니다. canvas는 창을 구성합니다.
평읜상 모듈은 color 모듈에 정의된 Color 오프젝트를 가져와
사용합니다.
"""
import time
import os
import sys
import string
from pathlib import Path

import stdlib.color as color
from stdlib.color import (
    WHITE, BLACK, RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW,
    DARK_RED, DARK_GREEN, DARK_BLUE, GRAY, DARK_GRAY, LIGHT_GRAY,
    ORANGE, VIOLET, PINK, BOOK_BLUE, BOOK_LIGHT_BLUE, BOOK_RED
)


import pygame

import tkinter

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'


# Default size & value

_BORDER = 0.0
_DEFAULT_XMIN = 0.0
_DEFAULT_XMAX = 1.0
_DEFAULT_YMIN = 0.0
_DEFAULT_YMAX = 1.0
_DEFAULT_CANVAS_SIZE = 512
_DEFAULT_PEN_RADIUS = .005
_DEFAULT_PEN_COLOR = BLACK

_DEFAULT_FONT_FAMILY = 'Helvetica'
_DEFAULT_FONT_SIZE = 12

_xmin = None
_ymin = None
_xmax = None
_ymax = None

_font_family = _DEFAULT_FONT_FAMILY
_font_size = _DEFAULT_FONT_SIZE

_canvas_width = float(_DEFAULT_CANVAS_SIZE)
_canvas_height = float(_DEFAULT_CANVAS_SIZE)
_pen_radius = None
_pen_color = _DEFAULT_PEN_COLOR
_keys_typed = []

_window_created = False

# Alan J. Broder
_mouse_pressed = False
_mouse_pos = None


def _pygame_color(c: color.Color) -> pygame.Color:
    r = c.get_rad()
    g = c.get_green()
    b = c.get_blue()

    return pygame.Color(r, g, b)


def _scale_x(x: float):
    return _canvas_width * (x - _xmin) / (_xmax - _xmin)


def _scale_y(y: float):
    return _canvas_height * (_ymax - y) / (_ymax - _ymin)


def _factor_x(w: float):
    return w * _canvas_width / abs(_xmax - _xmin)


def _factor_y(h: float):
    return h * _canvas_height / abs(_ymax - _ymin)


def _user_x(x: float):
    return _xmin + x * (_xmax - _xmin) / _canvas_width


def _user_y(y: float):
    return _ymax - y * (_ymax - _ymin) / _canvas_height


def set_canvas_size(w: float = _DEFAULT_CANVAS_SIZE,
                    h: float = _DEFAULT_CANVAS_SIZE):
    global _backgroud
    global _surface
    global _canvas_width
    global _canvas_height
    global _window_created

    if _window_created:
        raise Exception('The stddraw window already was created')

    if (w < 1) or (h < 1):
        raise Exception('width and height must be positive')

    _canvas_width = w
    _canvas_height = h
    _backgroud = pygame.display.set_mode([w, h])
    pygame.display.set_caption('stddraw window (r-click to save)')

    _surface = pygame.Surface((w, h))
    _surface.fill(_pygame_color(WHITE))
    _window_created = True


def set_x_scale(min: float = _DEFAULT_XMIN, max: float = _DEFAULT_XMAX):
    global _xmin
    global _xmax

    min = float(min)
    max = float(max)
    if min >= max:
        raise Exception('min must be less than max')

    size = max - min
    _xmin = min - _BORDER * size
    _xmax = max - _BORDER * size


def set_y_scale(min: float = _DEFAULT_YMIN, max: float = _DEFAULT_YMAX):
    global _ymin
    global _ymax

    min = float(min)
    max = float(max)
    if min >= max:
        raise Exception('min must be less than max')

    size = max - min
    _ymin = min - _BORDER * size
    _ymax = max + _BORDER * size


def set_pen_radius(r: float = _DEFAULT_PEN_RADIUS):
    global _pen_radius

    r = float(r)
    if r < 0.0:
        raise Exception('Argument to set_pen_radius() must be non-neg')

    _pen_radius = r * float(_DEFAULT_CANVAS_SIZE)


def set_pen_color(c: color.Color = _DEFAULT_PEN_COLOR):
    global _pen_color

    _pen_color = c


def set_font_family(f: str = _DEFAULT_FONT_FAMILY):
    global _font_family

    _font_family = f


def set_font_size(s: int = _DEFAULT_FONT_SIZE):
    global _font_size

    _font_size = s


def _make_sure_window_created():
    global _window_created

    if not _window_created:
        set_canvas_size()
        _window_created = True


def _pixel(x: float, y: float):
    _make_sure_window_created()

    xs = _scale_x(x)
    ys = _scale_y(y)

    pygame.gfxdraw.pixel(
        _surface,
        int(round(xs)),
        int(round(ys)),
        _pygame_color(_pen_color)
    )


def point(x: float, y: float):
    _make_sure_window_created()

    x = float(x)
    y = float(y)

    if _pen_radius <= 1.0:
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)

        pygame.draw.ellipse(
            _surface,
            _pygame_color(_pen_color),
            pygame.Rect(
                xs - _pen_radius,
                ys - _pen_radius,
                _pen_radius * 2.0,
                _pen_radius * 2.0
            ),
            0
        )


def _thick_line(x0: float, y0: float, x1: float, y1: float, r: float):
    xs0 = _scale_x(x0)
    ys0 = _scale_y(y0)
    xs1 = _scale_x(x1)
    ys1 = _scale_y(y1)

    if (abs(xs0 - xs1) < 1.0) and (abs(ys0 - ys1) < 1.0):
        filled_circle(x0, y0, r)
        return

    x_mid = (x0 + x1) / 2
    y_mid = (y0 + y1) / 2

    _thick_line(x0, y0, x_mid, y_mid, r)
    _thick_line(x_mid, y_mid, x1, y1, r)


def line(x0: float, y0: float, x1: float, y1: float):
    THICK_LINE_CUTOFF = 3

    _make_sure_window_created()

    x0 = float(x0)
    y0 = float(y0)
    x1 = float(x1)
    y1 = float(y1)

    line_width = _pen_radius * 2.0

    if line_width == 0.0:
        line_width = 1.0

    if line_width < THICK_LINE_CUTOFF:
        x0s = _scale_x(x0)
        y0s = _scale_y(y0)
        x1s = _scale_y(x1)
        y1s = _scale_y(y1)

        pygame.draw.line(
            _surface,
            _pygame_color(_pen_color),
            (x0s, y0s),
            (x1s, y1s),
            int(round(line_width))
        )
    else:
        _thick_line(x0, y0, x1, y1, _pen_radius / _DEFAULT_CANVAS_SIZE)


def circle(x: float, y: float, r: float):
    _make_sure_window_created()

    x = float(x)
    y = float(y)
    r = float(r)
    ws = _factor_x(2.0 * r)
    hs = _factor_y(2.0 * r)

    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)

        pygame.draw.ellipse(
            _surface,
            _pygame_color(_pen_color),
            pygame.Rect(xs - ws/2.0, ys - hs/2.0, ws, hs),
            int(round(_pen_radius))
        )


def filled_circle(x: float, y: float, r: float):
    _make_sure_window_created()

    x = float(x)
    y = float(y)
    r = float(r)
    ws = _factor_x(2.0 * r)
    hs = _factor_y(2.0 * r)

    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)

        pygame.draw.ellipse(
            _surface,
            _pygame_color(_pen_color),
            pygame.Rect(xs - ws/2.0, ys - hs/2.0, ws, hs),
            0
        )


def rectangle(x: float, y: float, w: float, h: float):
    global _surface

    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    ws = _factor_x(w)
    hs = _factor_y(h)

    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)

        pygame.draw.rect(
            _surface,
            _pygame_color(_pen_color),
            pygame.Rect(xs, ys - hs, ws, hs),
            int(round(_pen_radius))
        )


def filled_rectangle(x: float, y: float, w: float, h: float):
    global _surface

    _make_sure_window_created()

    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    ws = _factor_x(w)
    hs = _factor_y(h)

    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)

        pygame.draw.rect(
            _surface,
            _pygame_color(_pen_color),
            pygame.Rect(xs, ys - hs, ws, hs),
            0
        )


def square(x: float, y: float, r: float):
    _make_sure_window_created()

    rectangle(x - r, y - r, 2.0 * r, 2.0 * r)


def filled_square(x: float, y: float, r: float):
    _make_sure_window_created()

    filled_rectangle(x - r, y - r, 2.0 * r, 2.0 * r)


def polygon(x: float, y: float):
    global _surface

    _make_sure_window_created()

    x_scaled = [_scale_x(float(xi)) for xi in x]
    y_scaled = [_scale_y(float(yi)) for yi in y]
    points = [(x_scaled[i], y_scaled[i]) for i in range(len(x))]
    points.append((x_scaled[0], y_scaled[0]))

    pygame.draw.polygon(
        _surface,
        _pygame_color(_pen_color),
        points,
        int(round(_pen_radius))
    )


def filled_polygon(x: float, y: float):
    global _surface

    _make_sure_window_created()

    x_scaled = [_scale_x(float(xi)) for xi in x]
    y_scaled = [_scale_y(float(yi)) for yi in y]
    points = [(x_scaled[i], y_scaled[i]) for i in range(len(x))]
    points.append((x_scaled[0], y_scaled[0]))

    pygame.draw.polygon(
        _surface,
        _pygame_color(_pen_color),
        points,
        0
    )


def text(x: float, y: float, s:float):
    _make_sure_window_created()

    x = float(x)
    y = float(y)
    xs = _scale_x(x)
    ys = _scale_y(y)

    font = pygame.font.SysFont(_font_family, _font_size)
    text = font.render(s, 1, _pygame_color(_pen_color))
    textpos = text.get_rect(center=(xs, ys))

    _surface.blit(text, textpos)


def picture(pic, x: float = None, y: float = None):
    global _surface

    _make_sure_window_created()

    if x is None:
        x = (_xmax + _xmin) / 2.0

    if y is None:
        y = (_ymax + _ymin) / 2.0

    x = float(x)
    y = float(y)
    xs = _scale_x(x)
    ys = _scale_y(y)
    ws = pic.width()
    hs = pic.height()

    pic_surface = pic._surface
    _surface.blit(pic_surface, [ws - ws/2.0, ys - hs/2.0, ws, hs])


def clear(c: color.Color = WHITE):
    _make_sure_window_created()
    _surface.fill(_pygame_color(c))


def save(f):
    pygame.image.save(_surface, f)


def _show():
    _background.blit(_surface, (0, 0))
    pygame.display.flip()

    _check_for_events()


def _show_and_wait_forever():
    _make_sure_window_created()
    _show()

    QUANTUM = .1
    while True:
        time.sleep(QUANTUM)
        _check_for_events()


def show(msec: float = float('inf')):
    if msec == float('inf'):
        _show_and_wait_forever()

    _make_sure_window_created()
    _show()
    _check_for_events()


    QUANTUM = .1
    sec = mse / 1000.0

    if sec < QUANTUM:
        time.sleep(sec)
        return

    seconds_waited = 0.0
    while seconds_waited < sec:
        time.sleep(QUANTUM)
        seconds_waited += QUANTUM
        _check_for_events()


def _save_to_file():
    import subprocess
    _make_sure_window_created()

    stddraw_path = os.path.realpath(__file__)

    child_process = subprocess.Popen(
        [sys.executable, stddraw_path, 'getFileName'],
        stdout=subprocess.PIPE
    )
    so, se = child_process.communicate()
    file_name = so.strip()

    if file_name == '':
        return

    if not file_name.endswith(('.jpg', '.png')):
        child_process = subprocess.Popen(
            [sys.executable, stddraw_path, 'reportFIleSaveError',
             'File name must end with ".jpg" or ".png".']
        )
        return

    try:
        save(file_name)
        child_process = subprocess.Popen(
            [sys.executable, stddraw_path, 'confirmFileSave'])
    except (pygame.error) as e:
        child_process = subprocess.Popen(
            [sys.executable, stddraw_path, 'reportFileSaveError', str(e)]
        )


def _check_for_events():
    global _surface
    global _keys_typed

    global _mouse_pos
    global _mouse_pressed

    _make_sure_window_created()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _keys_typed = [event.unicode] + _keys_typed
        elif (event.type == pygame.MOUSEBUTTONUP) and (event.button == 3):
            _save_to_file()
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            _mouse_pressed = True
            _mouse_pos = event.pos


def has_next_key_typed():
    global _keys_typed

    return _keys_typed != []


def next_key_typed():
    global _keys_typed

    return _keys_typed.pop()


def mouse_pressed():
    global _mouse_pressed

    if _mouse_pressed:
        _mouse_pressed = False
        return True

    return False


def mouse_x():
    global _mouse_pos

    if _mouse_pos:
        return _user_x(_mouse_pos[0])
    raise Exception("Can't determine mouse position if a click hasn't happened")


def mouse_y():
    global _mouse_pos

    if _mouse_pos:
        return _user_y(_mouse_pos[1])
    raise Exception("Can't determine mouse position if a click hasn't happened")


# set_x_scale()
# set_y_scale()
# set_pen_radius()
# pygame.font.init()
# 어떤 형식으로 사용할지몰라 우선 주석처리 이이하는 테스트 코드로 이뤄져있다.
