from pymongo import MongoClient
import pymongo
import time


client = MongoClient()
db = client.limdata
col = db.blog
#build the index for searching fast
col.create_index([('timestamp',pymongo.ASCENDING)])
total_num = col.count()
print "total_num: ",total_num

time_delta_list = []
# set the first second as the earliest time
second1 = 23 * 3600 + 0 + 0
data = col.find().sort('timestamp',pymongo.ASCENDING)
for item in data:
	data_time = time.strptime(item['timestamp'],"%Y-%m-%d %H:%M:%S")
	#print data_time
	#print data_time.tm_mday,data_time.tm_hour,data_time.tm_min,data_time.tm_sec
	#calculate from 2015-6-22 00:00:00 
	second2 = (data_time.tm_mday-22)*86400 + (data_time.tm_hour * 3600) +(data_time.tm_min*60) + data_time.tm_sec
	delta = second2 - second1
	second1 = second2
	time_delta_list.append(delta)
print 'mean_time_delta: ',float(sum(time_delta_list)) / (len(time_delta_list)-1),'s'


