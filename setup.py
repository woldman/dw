#!/usr/bin/env python
#
# Copyright Oscar Benjamin 2011 under GPLv3+

from distutils.core import setup
from distutils.extension import Extension
from distutils.cygwinccompiler import Mingw32CCompiler # ming32 fix
from Cython.Distutils import build_ext

import numpy


ext_modules = [
    Extension('dw', ['dw.pyx', '../sode_new/sode/cfiles/randnorm.c'],
include_dirs=[numpy.get_include(), '../sode_new'], libraries = ['m']),
]

# Standard distutils setup
setup(
    # Now the content
    cmdclass = {'build_ext':build_ext},
    ext_modules = ext_modules,
)
