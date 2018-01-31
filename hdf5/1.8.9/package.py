# -*- coding: utf-8 -*-

name = 'hdf5'

version = '1.8.9'

variants = [['platform-linux', 'arch-x86_64']]

def commands():
    appendenv('HDF5_ROOT', '{root}')

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.HDF5_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")


