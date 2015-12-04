from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client.limdata
col = db.blog
#build the index for searching fast
col.create_index([('id_member',pymongo.ASCENDING)])

print "total: ",col.count(10)

data = col.find()

member_list = []
n = 0


for item in data:
	for id_num in member_list:
		if id_num == item['id_member']:
			break
	else:
		member_list.append (item['id_member'])


	
num_menber = len(member_list)

print "num_menber: ", num_menber





			



