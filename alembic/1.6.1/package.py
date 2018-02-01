# -*- coding: utf-8 -*-

name = 'alembic'

version = '1.6.1'

build_requires = [
    'boost-1.55',
    'ilmbase',
    'pyilmbase',
]

variants = [
    ['platform-linux', 'arch-x86_64'],
]


def commands():
    appendenv('PATH', '{root}/bin/')
    appendenv('PYTHONPATH', '{root}/lib/')

    if building:
        appendenv('LD_LIBRARY_PATH', '{root}/lib/')
