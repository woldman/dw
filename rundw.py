#!/usr/bin/env python

from dw import DoubleWell

import sys
from sode.script import Script
script = Script(DoubleWell)
script.main(argv=sys.argv[1:])
