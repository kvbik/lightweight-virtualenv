
import sys
from os.path import dirname, join, exists
from os import makedirs

base = dirname(__file__)

# create lib subdir
site_packages = join(base, 'lib', 'python%s' % sys.version[:3], 'site-packages')
if not exists(site_packages):
    makedirs(site_packages)

# check whether you are in virtualenv
#print 'virtual environment enabled :: takze dobry vecer...'

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

