# -*- coding: utf-8 -*-

name = 'boost'

version = '1.55.0'

variants = [['platform-linux', 'arch-x86_64']]

def commands():
    appendenv('BOOST_ROOT', '{root}')
    if building:
        appendenv('LD_LIBRARY_PATH', '{root}/lib/')


