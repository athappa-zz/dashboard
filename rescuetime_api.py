#Access the Rescuetime API 

'''
The idea of this is to first pull in my rescuetime data.
After doing this, I want to display some summary statistics
on an HTML page online. 

Before running:
1. Go to command line and run 'pip install requests'

Source URL:
https://www.rescuetime.com/anapi/data?rtapi_key=B63NUgr1wbXQS_I6tT8ON0LpvyPPcXNOd1mXfrG9&perspective=interval&format=json&resolution_time=hour&restrict_kind=activity&restrict_begin=2013-01-01&restrict_end=2014-09-12%22
'''


#Import the proper modules
import json
import requests
from datetime import (time,
		date,
		)

def download_rescuetime_json():
#Rescuetime URL information 
	api_key_personal = 'B63oG9iv9vCP8cdV2TrXIsqsN1YmhswhxcCBHafi'
	api_key_stack = 'B63NUgr1wbXQS_I6tT8ON0LpvyPPcXNOd1mXfrG9'
	format = 'json'
	begin_date = '2013-01-01'
	end_date = date.today().isoformat()
	url = 'https://www.rescuetime.com/anapi/data?rtapi_key='+api_key_personal+'&perspective=interval&format='+format+'&resolution_time=hour&restrict_kind=activity&restrict_begin='+begin_date+'&restrict_end='+end_date+'%22'

	#Download the webpage which has notes, row_headers, and rows
	#Requests will return a response object so call var.text for the actual data
	rescuetime = requests.get(url)
	rescuetime_raw = rescuetime.text

	#This loads the data
	rescuetime_json_dict = json.loads(rescuetime_raw)
	rescuetime_json_raw = rescuetime.json()

	rescuetime_json_split_dates = [item[0].split('T') + item[1:] for item in rescuetime_json_raw['rows']]
	#print rescuetime_json_split_dates
	return rescuetime_json_split_dates 

#download_rescuetime_json()



'''
Things to add eventually:
1. Pandas dataframe capabilities
	-import pandas
	-rescuetime_dataframe = pandas.read_json(rescuetime_raw)
	-pip install pandas --upgrade

Questions:
1. Is the data I'm looking at in the website, raw JSON or is it 
a JSON dictionary or something different? It seems to have some 
notes at the header. Do I need to index it in some way?

http://jinja.pocoo.org/docs/dev/
https://realpython.com/blog/python/primer-on-jinja-templating/

this looks good too:
http://python.zirael.org/e-jinja1.html

http://www.openbookproject.net/books/bpp4awd/
https://www.udemy.com/web-programming-with-python/
'''


