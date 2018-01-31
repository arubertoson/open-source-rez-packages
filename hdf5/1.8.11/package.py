# -*- coding: utf-8 -*-

name = 'hdf5'

version = '1.8.11'

variants = [
    ['platform-linux', 'arch-x86_64'],
]


def commands():
    appendenv('HDF5_ROOT', '{root}')

    if building:
        env.HDF5_INCLUDE_DIR = "{root}/include"
        env.LD_LIBRARY_PATH.append("{root}/lib")
