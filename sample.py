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
db_client = MongoClient()

db = db_client.switch_db
col = db.deals



print(db.col.find_one())

