
from os.path import dirname, join

base = dirname(__file__)

# check whether you are in virtualenv
#print 'virtual environment enabled with mocked datetime'

# activate virtualenv
activate_this = join(base, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# mock up datetime
import datetime, time
mytime = 423592200 # 1983/6/4 0:30 CEST
mydatetime = datetime.datetime.fromtimestamp(mytime)
old_localtime = time.localtime
class NewDatetime(datetime.datetime):
    @classmethod
    def now(cls):
        return mydatetime
def new_time():
    return mytime
def new_localtime(seconds=None):
    if not seconds:
        return mydatetime.timetuple()
    return old_localtime(seconds)
datetime.datetime = NewDatetime
time.time = new_time
time.localtime = new_localtime

