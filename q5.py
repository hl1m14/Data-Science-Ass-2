import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pymongo import MongoClient

client = MongoClient()
db = client.limdata
col = db.blog
#build the index for searching fast
total_num = col.count()
print "total_num: ",total_num

lenth_list = []
data = col.find()
for item in data:
	lenth_list.append(len(str(item['text'])))
print "message_mean_length: ", float(sum(lenth_list))/len(lenth_list)







