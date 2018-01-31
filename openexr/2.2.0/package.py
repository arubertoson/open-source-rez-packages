# -*- coding: utf-8 -*-

name = 'openexr'

version = '2.2.0'

build_requires = [
    'ilmbase',
]

variants = [
    ['platform-linux', 'arch-x86_64'],
]


def commands():
    appendenv('PATH', '{root}/bin/')
    setenv('OPENEXR_ROOT', '{root}')

    if building:
        appendenv('LD_LIBRARY_PATH', '{root}/lib/')
        appendenv('PKG_CONFIG_PATH', '{root}/lib/pkgconfig/')
