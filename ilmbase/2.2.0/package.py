# -*- coding: utf-8 -*-

name = 'ilmbase'

version = '2.2.0'

variants = [['platform-linux', 'arch-x86_64']]

def commands():
    appendenv('ILMBASE_ROOT', '{root}')

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.ILMBASE_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")


