import pymongo
from pymongo import MongoClient
# import pprint
from pprint import pprint as pp
from json_handler import post_dic

def mongoCleaner(key):
	return key.replace(".", " ", len(key))
def updateMongo():
	for sub in post_dic:
		dic = {"name": mongoCleaner(sub), "seen": post_dic[sub]}
		db.col.insert_one(dic)
# pp = pprint.pprint
client = MongoClient()

db = client.pymongo_db
col = db.pymongo_col


item = db.col.find_one({"error": "1"})
pp(item)
if item == None:
	print("not in there")
else:
	print("in there")

