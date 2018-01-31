# -*- coding: utf-8 -*-

name = 'ffmpeg'

version = '3.3.5'

variants = [
    ['platform-linux', 'arch-x86_64'],
]


def commands():
    env.PATH.append('{root}/bin')

    if building:
        appendenv('PKG_CONFIG_PATH', '{root}/lib/pkgconfig/')
