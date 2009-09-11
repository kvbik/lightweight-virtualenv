
from os.path import dirname, join

# at vime, ze jsem to ja
print 'takze dobry vecer'

base = dirname(__file__)

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

