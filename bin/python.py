#!/usr/bin/env python

'''
use this file directly, or just set PYTHONPATH to your virtualenv directory
and run system wide python instance
'''

import os, sys
from os.path import join, dirname, pardir, abspath
import subprocess

def get_this_path():
    base = dirname(__file__)
    thispath = abspath(join(base, pardir))
    return thispath

def inject_pythonpath():
    '''
    insert current path into pythonpath
    '''
    pypath = os.environ.get('PYTHONPATH', '').split(':')
    thispath = get_this_path()
    try:
        pypath.remove('')
        pypath.remove(thispath)
    except ValueError:
        pass
    pypath.insert(0, thispath)
    os.environ['PYTHONPATH'] = ':'.join(pypath)

def prepare_command():
    '''
    prepare command to run
    '''
    cmd = ['python'] + sys.argv[1:]
    cmd = map(lambda s: '"%s"' % s.replace('"', '\\"'), cmd)
    cmdstr = ' '.join(cmd)
    return cmdstr

inject_pythonpath()
os.system(prepare_command())

