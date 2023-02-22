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

mydict = { "name": "John", "role": "Highway 37" }


"""insert_one() this method used to insert the data in data base where it retrieve the id of the inserted document"""
"""mycol is the collection(table)"""

x = mycol.insert_one(mydict)

print(x)
"""assign unique id for the values"""
print(x.inserted_id)

mylist=[
  {'name': 'bruse wayne','role':'batman'},
  {'name': 'alfred pennyworth','role':'body guard'},
  {'name': 'salena kyle','role':'bat women'},
  {'name': 'penguin','role':'thug'},
  {'name': 'harvey dent','role':'mayor'},
]

y=mycol.insert_many(mylist)
print("multiple documents ",y)
