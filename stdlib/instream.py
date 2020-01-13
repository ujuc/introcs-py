"""
instream.py

``instream`` 모듈은 InStream 클래스를 정의한다.
"""

import sys
import urllib.request as urllib
import re


class InStream:
    """
    InStream 오브젝트는 텍스트 파일이나 sys.stdin 를 랩핑한뒤
    stream을 통해 읽어오는 것을 지원한다.
    """

    def __init__(self, file_or_url=None):
        self._buffer = ''
        self._stream = None
        self._reading_web_page = False

        if file_or_url is None:
            import stdlib.stdio as stdio
            self._stream = sys.stdin
            return

        try:
            self._stream = urllib.urlopen(file_or_url)
            self._reading_web_page = True
        except IOError:
            raise IOError(f'No such file or URL: {file_or_url}')

    def _read_reg_exp(self, reg_exp):
        if self.is_empty():
            raise EOFError()

        compiled_reg_exp = re.compile(r'^\s*' + reg_exp)
        match = compiled_reg_exp.search(self._buffer)
        if match is None:
            raise ValueError()

        s = match.group()
        self._buffer = self._buffer[match.end():]

        return s.lstrip()

    def is_empty(self):
        while self._buffer.strip() == '':
            line = self._stream.readline()
            if line == '':
                return True

            self._buffer += str(line)

        return False

    def read_int(self):
        s = self._read_reg_exp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
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

    def read_all_ints(self):
        strings = self.read_all_strings()

        return [int(s) for s in strings]

    def read_float(self):
        s = self._read_reg_exp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')

        return float(s)

    def read_all_floats(self):
        strings = self.read_all_strings()

        return [float(s) for s in strings]

    def read_bool(self):
        s = self._read_reg_exp(r'(True)|(False)|1|0')

        if (s == 'True') or (s == '1'):
            return True

        return False

    def read_all_bools(self):
        strings = self.read_all_strings()

        return [bool(s) for s in strings]

    def read_strings(self):
        s = self._read_reg_exp(r'\S+')

        return s

    def read_all_strings(self):
        strings = []

        while not self.is_empty():
            s = self.read_strings()
            strings.append(s)

        return strings

    def has_next_line(self):
        if self._buffer != '':
            return True

        self._buffer = self._stream.readline()
        if self._buffer == '':
            return False

        return True

    def read_line(self):
        if not self.has_next_line():
            raise EOFError

        s = self._buffer
        self._buffer = ''

        return s.rstrip('\n')

    def read_all_lines(self):
        lines = []
        while self.has_next_line():
            line = self.read_line()
            lines.append(line)

        return lines

    def read_all(self):
        s = self._buffer
        self._buffer = ''

        for line in self._stream:
            s += line

        return s

    def __del__(self):
        if self._stream is not None:
            self._stream.close()
