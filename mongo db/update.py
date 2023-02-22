import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


'''change only 1 occurrence'''
myquery = { "role": "batman" }
newvalues = { "$set": { "name": "the dark knight" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)


#chage the name whose roles are start with b
myquery = { "role": { "$regex": "^b" } }
newvalues = { "$set": { "name": "team batman" } }

x = mycol.update_many(myquery, newvalues)


print(x.modified_count, "documents updated.")

for m in mycol.find():
  print("after updating ",m)
