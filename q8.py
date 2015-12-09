import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pymongo import MongoClient
import pymongo
from bson.code import Code


client = MongoClient()
db = client.limdata
col = db.blog

print 'total_num :', col.count()


mapper = Code("""
	              function () {

	               	var latitude = Math.round(this.geo_lat/2)*2;
	               	var longitude = Math.round(this.geo_lng/2)*2;

	               	var block = latitude + ':' + longitude;
	               	emit(block,1);

	              }
	              """)

reducer = Code("""
	               function (block, values) {

	                  return Array.sum(values)

	               }
	                """)

result = col.map_reduce(mapper, reducer, "block_result_count")

col = db.block_result_count

col.create_index([('value',pymongo.DESCENDING)])
data = col.find().sort('value',pymongo.DESCENDING).limit(10)

for item in data:
	print item




