
from os.path import dirname, join

base = dirname(__file__)

# check whether you are in virtualenv
print 'virtual environment enabled :: takze dobry vecer...'

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

'''
# mock up datetime
import datetime
old_datetime = datetime.datetime
class NewDatetime(datetime.datetime):
    @classmethod
    def now(cls):
        return cls(1983, 6, 4)
datetime.datetime = NewDatetime
'''

