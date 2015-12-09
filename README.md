# Data-Science-Ass-2
Assignment 2 about the mongoDB

Pipeline :

(1)Import the data into mongodb locally with the database named ‘limdata’ and collection named ‘blog’ . Do the data cleaning later in the code of querying.
>>> mongoimport --db limdata --collection blog --type csv --headerline --file microblogDataset_COMP6235_CW2.csv

(2)Run file ‘q1and2.py’ to solve query 1 and query 2, which connects to the mongodb and makes an aggregations operation as a pipeline to group ‘id_menber’ and count the number of same id_menber, then sort the result by count.
	(data = col.aggregate([{"$group":{'_id':"$id_member",'count':{"$sum":1}}},{"$sort":{'count': -1}}]))
the quantity of results is the answer for query 1.
the sum of ‘count’ of top 10 ‘id_member’ is the answer for query 2.

(3)Run file ‘q3.py’ to solve query 3, which connects to the mongodb and creates an index on ‘timestamp’, then sort all data by ‘timestamp’ to get the earliest and latest time.
(col.create_index([(‘timestamp',pymongo.ASCENDING)])
data = col.find().limit(1).sort(‘timestamp',pymongo.ASCENDING)
data = col.find().limit(1).sort('timestamp',pymongo.DESCENDING))


(4)Run file ‘q4.py’ to solve query 4, which connects to the mongodb then searches all the timestamps and converts these to seconds for being convenient  to calculate the mean time delta between all messages.

(5)Run file ‘q5.py’ to solve query 5, which connects to the mongodb, finds all texts and converts all texts to strings in case there are some wrong type texts then calculates the mean length of a message.

(6) Run file ‘q6_1.py’ to get the 10 most common unigram strings, it uses two MapReduces, first one splits the message into unigram strings, the second one maps 1 to every unigram string, then count the sum. Then sort the results by the ‘sum’, getting the top 10. 
   Run file ‘q6_2.py’ to get the 10 most common bigram strings,  the structure is similar with ‘q6_1.py’, the only little difference is splitting the message by two characters.
(These two processes may take a bit long time.)

(7)Run file ‘q7.py’ to solve query 7, which connects to mongodb and creates a text index on ‘text’, then finds all messages that contain ‘#’, the next step is counting the number of ‘#’ within a message, finally computes the sum and the mean.

(8)Run file ‘q8.py’ to solve query 8, which connects to mongodb and uses MapReduce, aggregating latitude and longitude as blocks each covering 2 latitudes and 2 longitudes, mapping 1 to every block, then count the sum of every block, sort the results by count and get the top one.
 