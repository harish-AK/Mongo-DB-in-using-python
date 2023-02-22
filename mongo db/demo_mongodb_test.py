import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print("data bases are : ",myclient.list_database_names()) 


"""used to list out my mongo db data bases"""


dblist = myclient.list_database_names()  

"""check whether my mongo db database is created or not"""


if "mydatabase" in dblist:
  print("         The database exists.")
else:                                                                
  print("data base not exists")  

  """" output is database not exists cause in mongo db db will be shown once the data is inserted"""



"""create a collection"""

mycol = mydb["customers"]

print("collections are ",mydb.list_collection_names())

collist = mydb.list_collection_names()


if "customers" in collist:
  print("        The collection exists.")
else:
  print("collection not existed")



"""insert data"""

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)

print(x.inserted_id)
