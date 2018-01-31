# -*- coding: utf-8 -*-

name = 'ilmbase'

version = '2.2.1'

variants = [
    ['platform-linux', 'arch-x86_64'],
]


def commands():
    appendenv('ILMBASE_ROOT', '{root}')

    if building:
        env.LD_LIBRARY_PATH.append("{root}/lib")
        env.ILMBASE_INCLUDE_DIR = "{root}/include"
