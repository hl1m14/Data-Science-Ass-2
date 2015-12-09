from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client.limdata
col = db.blog

total_num = col.count()
print "total_num: ",total_num

data = col.aggregate([{"$group":{'_id':"$id_member",'count':{"$sum":1}}},{"$sort":{'count': -1}}])

dup_num = []
n = 0
for item in data:
	n = n + 1
	dup_num.append(item['count'])
print 'unique_idmember_num: ' ,n
print 'tweets_of_top_ten: ', sum(dup_num[0:10])
print 'percent: ',float(sum(dup_num[0:10]))/total_num * 100,'%'





