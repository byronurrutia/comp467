# Mondo Database DB Tutorial (local machine)
# https://www.w3schools.com/python/python_mongodb_getstarted.asp
# Do:
# -Get started
# -Create database
# -Create Collections
# -Insert

 

# -Print console output from all 4 once completed as submission
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://burrutia:<password>@seniorproject-west.ralsx.mongodb.net/test")

mydb = myclient["mydatabase"]
mycol = mydb["mycollection"]

mydata = []

for i in range(20):
    mydata.append({
        "_id": i, "name": "chaja" + str(i), "coolness lvl": i
    })

x = mycol.insert_many(mydata)

print(myclient.list_database_names())
print(mydb.list_collection_names())

for x in mycol.find():
  print(x)