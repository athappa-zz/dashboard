import json
import pandas
import numpy as np
import matplotlib.pyplot as plt
from ggplot import *
import rescuetime_api as api
from datetime import (time,
		date,
		timedelta
		)


#Import the raw json from the rescuetime_api.py data
raw_json = api.download_rescuetime_json()


#find all the data from today
today = date.today().isoformat()
today_raw_json = [i for i in raw_json if i[0] == today]


df = pandas.DataFrame(today_raw_json)
#df = pandas.DataFrame(raw_json)
df.columns = ['date', 'time', 'seconds_spent', 'number_users', 'activity', 'category', 'productivity']


plt.ion()


df['date'] = pandas.to_datetime(df['date']+df['time'],format='%Y-%m-%d%H:%M:%S')
df=df.set_index(['date'])
rng = pandas.date_range('9/26/2014 00:00:00',periods=24,freq='H')
N = np.arange(len(rng))


# Grab only records where category is email:
def make_data(category):
	b = df['productivity']==category
	# Create a time series object just for email:
	data = df['seconds_spent'][b]
	data = data.groupby(data.index).sum()
	# Now fill in the blanks for missing email values:
	A = data.reindex(rng)
	A = A.fillna(0)
	return A

a=list(set(df['productivity']))
a
things_to_plot = a[0:]
for a_thing in things_to_plot:
	p = plt.bar(N, make_data(a_thing), color=np.random.rand(3,1))

plt.legend(a,bbox_to_anchor = (0.5,1))
#p1 = plt.bar(N,email,color=np.random.rand(3,1))
#p2 = plt.bar(N,search,color='y')

plt.show()

