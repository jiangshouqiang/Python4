import pymongo

conn = pymongo.Connection('127.0.0.1',27017)
db = conn.tage
db.user.save({'id':1,'name':'jiang'})