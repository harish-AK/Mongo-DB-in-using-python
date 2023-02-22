import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

'''display the values'''

x = mycol.find_one()

print(x)



'''to get multiple values use iteration'''
for i in mycol.find():
    print(i)

'''run specific fields alone'''
for a in mycol.find({},{ "name": 1, "address": 1 }):
  print(a)

'''excluding role(0 means exclude)'''
for x in mycol.find({},{ "role": 0 }):
   print(x)




