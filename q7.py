import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pymongo import MongoClient
import pymongo


client = MongoClient()
db = client.limdata
col = db.blog
#build the text index for searching fast
col.create_index([('text', 'text')])
total_num = col.count()
print "total_num: ",total_num

data = col.find({"text": {'$regex' : '.*' + '#' + '.*'}})

num_hashtags_list =[]

for item in data:
	num_hashtags_list.append(item['text'].count('#'))

print "average_num_hashtags:" ,float(sum(num_hashtags_list))/total_num


