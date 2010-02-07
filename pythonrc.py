
from os.path import dirname, join, exists
import distutils.command.install

# check whether you are in virtualenv
#print 'virtual environment enabled :: takze dobry vecer...'

base = dirname(__file__)

# set correct install schemes
SCHEME = {
    'purelib': '$base/lib/site-packages',
    'platlib': '$base/lib/site-packages',
    'headers': '$base/include/$dist_name',
    'scripts': '$base/bin',
    'data'   : '$base',
}
schemes = distutils.command.install.INSTALL_SCHEMES
for k in schemes.keys():
    schemes[k] = SCHEME

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

