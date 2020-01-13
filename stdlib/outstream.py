"""
outstream.py

``outstream`` 모듈은 OutStream 클래스를 정의한다.
"""

import sys


class OutStream:
    """
    출력에 관련된 것들을 정의한다.
    """

    def __init__(self, f=None):
        if f is None:
            self._stream = sys.stdout
        else:
            self._stream = open(f, 'w', encoding='utf-8')

    def writeln(self, x=''):
        x = str(x)
        self._stream.write(x)
        self._stream.write('\n')
        self._stream.flush()

    def write(self, x=''):
        x = str(x)
        self._stream.write(x)
        self._stream.flush()

    def writef(self, fmt, *args):
        x = fmt % args
        self._stream.write(x)
        self._stream.flush()

    def __del__(self):
        self._stream.close()
