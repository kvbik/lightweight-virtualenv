
import distutils.spawn
from os.path import dirname, join, exists
import distutils.command.install

# check whether you are in virtualenv
#print 'virtual environment enabled :: takze dobry vecer...'

base = dirname(__file__)

# set correct install schemes
SCHEME = {
    'purelib': '$base/lib/python/site-packages',
    'platlib': '$base/lib/python/site-packages',
    'headers': '$base/include/$dist_name',
    'scripts': '$base/bin',
    'data'   : '$base',
}
schemes = distutils.command.install.INSTALL_SCHEMES
for k in schemes.keys():
    schemes[k] = SCHEME

# do not spawn with -E argument
def spawn (cmd,
           search_path=1,
           verbose=0,
           dry_run=0):
    if '-E' in cmd:
        cmd.remove('-E')
    distutils.spawn._spawn(cmd, search_path, verbose, dry_run)
distutils.spawn._spawn = distutils.spawn.spawn
distutils.spawn.spawn = spawn

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

