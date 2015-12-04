from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client.limdata
col = db.blog
#build the index for searching fast
col.create_index([('timestamp',pymongo.ASCENDING)])

print "total_num: ",col.count()

data = col.find().limit(1).sort('timestamp',pymongo.ASCENDING)

for item in data:
	print 'earliest date :',item['timestamp']

data = col.find().limit(1).sort('timestamp',pymongo.DESCENDING)

for item in data:
	print 'latest date :',item['timestamp']

