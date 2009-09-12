
from os.path import dirname, join

base = dirname(__file__)

# check whether you are in virtualenv
print 'virtualn environment enabled :: takze dobry vecer...'

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

