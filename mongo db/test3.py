import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "role": "batman" }


'''specify the data from collection'''

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

''' getting whose roles are starts with b or higher'''
myquery = { "role": { "$gt": "b" } }

mydoc = mycol.find(myquery)
for d in mydoc:
  print("b or higer ",d)


myquer = { "role": { "$regex": "^b" } }

mydo = mycol.find(myquer)

for xx in mydo:
  print("starts with b ",xx)

