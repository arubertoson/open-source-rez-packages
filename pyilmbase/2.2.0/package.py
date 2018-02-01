# -*- coding: utf-8 -*-

name = 'pyilmbase'

version = '2.2.1'

build_requires = [
    'boost',
    'python',
    'numpy',
    'ilmbase',
]

variants = [
    ['platform-linux', 'arch-x86_64'],
]


def commands():
    appendenv('PYTHONPATH', '{root}/lib64/python2.7/site-packages')

    if building:
        appendenv('LD_LIBRARY_PATH', '{root}/lib/')
        appendenv('PKG_CONFIG_PATH', '{root}/lib/pkgconfig/')
