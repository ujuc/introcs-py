"""
stdaudio.py

``stdaudio`` 모듈은 오디오를 사용하는 기능을 정의해둔다.
"""

import sys

import numpy
import pygame

import stdlib.stdio as stdio

_SAMPLES_PER_SECOND = 44100
_SAMPLES_SIZE = 16
_CHANNEL_COUNT = 1
_AUDIO_BUFFER_SIZE = 1024
_CHECK_RATE = 44100

_my_buffer = []
_MY_BUFFER_MAX_LENGTH = 4096


def wait():
    global _channel

    clock = pygame.time.Clock()

    while _channel.get_queue() is not None:
        clock.tick(_CHECK_RATE)


def play_sample(s):
    global _my_buffer
    global _channel

    _my_buffer.append(s)
    if len(_my_buffer) > _MY_BUFFER_MAX_LENGTH:
        temp = [numpy.int16(sample * float(0x7fff)) for sample in _my_buffer]
        samples = numpy.array(temp, numpy.int16)
        sound = pygame.sndarray.make_sound(samples)

        wait()

        _channel.queue(sound)
        _my_buffer = []


def play_samples(a):
    for sample in a:
        play_sample(sample)


def play_array(a):
    play_samples(a)


def play_file(f):
    a = read(f)
    play_samples(a)


def save(f, a):
    import wave

    file_name = f + '.wav'
    temp = [int(sample * float(0x7fff)) for sample in a]
    samples = numpy.array(temp, numpy.int16)

    with wave.open(file_name, 'w') as file:
        file.setnchannels(_CHANNEL_COUNT)
        file.setsampwidth(2)
        file.setframerate(_SAMPLES_PER_SECOND)
        file.setnframes(len(samples))
        file.setcomptype('NONE', 'descrip')
        file.writeframes(samples.tostring())


def read(f):
    file_name = f + '.wav'
    sound = pygame.mixer.Sound(file_name)
    samples = pygame.sndarray.samples(sound)
    temp = [(float(samples[i]) / float(0x7fff)) for i in range(len(samples))]

    return temp


try:
    pygame.mixer.init(_SAMPLES_PER_SECOND, _SAMPLES_SIZE, _CHANNEL_COUNT,
                      _AUDIO_BUFFER_SIZE)
    _channel = pygame.mixer.Channel(0)
except pygame.error:
    stdio.writeln('Could not initialize PyGame')
    sys.exit(1)
