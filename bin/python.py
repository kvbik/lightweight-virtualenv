#!/usr/bin/env python

'''
use this file directly, or just set PYTHONPATH to your virtualenv directory
and run system wide python instance
'''

import os, sys
from os.path import join, dirname, pardir, abspath
import subprocess

base = dirname(__file__)
os.environ['PYTHONHOME'] = abspath(join(base, pardir))

cmd = ['python'] + sys.argv[1:]
try:
    subprocess.call(cmd)
except KeyboardInterrupt:
    pass

