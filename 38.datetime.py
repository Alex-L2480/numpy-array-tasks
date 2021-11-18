import numpy as np
yesterday = np.datetime64('today') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today     = np.datetime64('today')
print("Today: ",today)
tomorrow  = np.datetime64('today') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)