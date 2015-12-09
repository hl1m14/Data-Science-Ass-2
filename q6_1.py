import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pymongo import MongoClient
import pymongo
from bson.code import Code


client = MongoClient()

#for -- data
db = client.limdata
col = db.blog


total_num = col.count()
print "total_num: ",total_num

keys_list = []
data = col.find().limit(1)

for item in data:
  keys_list = item.keys()

if keys_list.count('mr_status'):
  if item['mr_status'] == 'processed':
    col.update_many({'mr_status':{'$exists':True}},{'$set':{'mr_status':"inprocess"}});
else:
  col.update_many({'mr_status':{'$exists':False}},{'$set':{'mr_status':"inprocess"}});

mapper = Code("""
	              function() {
        uniqueWords = function (words){
            var arrWords = words.split(" ");
            var arrNewWords = [];
            var seenWords = {};
            var arrNewWords2 = [];
            for(var i=0;i<arrWords.length;i++) {
                if (!seenWords[arrWords[i]]) {
                    seenWords[arrWords[i]]=true;
                    arrNewWords.push(arrWords[i]);
                }
            }

            return arrNewWords;
        }
      var unigrams =  uniqueWords(this.text) ;
      emit(this.id_member, {unigrams:unigrams});
};

	              """)

reducer = Code("""
	               function(key,values){

    Array.prototype.uniqueMerge = function( a ) {
        for ( var nonDuplicates = [], i = 0, l = a.length; i<l; ++i ) {
            if ( this.indexOf( a[i] ) === -1 ) {
                nonDuplicates.push( a[i] );
            }
        }
        return this.concat( nonDuplicates )
    };

    unigrams = [];
    values.forEach(function(i){
        unigrams = unigrams.uniqueMerge(i.unigrams);
    });
    return { unigrams:unigrams};
};
	                """)

result = col.map_reduce(mapper, reducer, "unigram_result",query = {'mr_status':"inprocess",'text':{'$type':2}})


col.update_many({'mr_status':"inprocess"},{'$set':{'mr_status':"processed"}});

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^step 2 : count^^^^^^^^^^^^^^^^^#

col = db.unigram_result

mapper = Code("""
                  function () {

                    this.value.unigrams.forEach(function(z) {
                      emit(z, 1);
                    });

                  }
                  """)

reducer = Code("""
                   function (key, values) {

                      var total = 0;
                      for (var i = 0; i < values.length; i++) {
                       total += values[i];
                      }
                      return total;

                   }
                    """)

result = col.map_reduce(mapper, reducer, "unigram_result_count")


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^step 3 : sort ^^^^^^^^^^^^^^^^^#

col = db.unigram_result_count

col.create_index([('value',pymongo.ASCENDING)])
data = col.find().sort('value',pymongo.DESCENDING).limit(11)


for item in data:
    print item


