import pymongo
# import os

# # Get the list of all files and directories
# path = "/home/byronurrutia/projects/comp467/project2"
# dir_list = os.listdir(path)

# print("Files and directories in '", path, "' :")

# # prints all files
# print(dir_list)

# 2. All work done before 3-25-2023 date on a Flame
# 3. What work done on hpsans13 on date 3-26-2023
# 4. Name of all Autodesk Flame users

myclient = pymongo.MongoClient(
    "mongodb+srv://test:eU2Lh8qXFHJF1Xet@seniorproject-west.ralsx.mongodb.net/test")
mydb = myclient["mydatabase"]
col1 = mydb["mycollection1"]
col2 = mydb["mycollection2"]

# 1. List all work done by user TDanza
print("List all work done by user TDanza: ")

myquery = {"file_username": "TDanza"}

mydoc = col2.find(myquery)

for x in mydoc:
    print(x)

# 2. All work done before 3-25-2023 date on a Flame
print("All work done before 3-25-2023 date on a Flame:")

myquery = {"machine": "Flame"}

mydoc = col1.find(myquery)

for x in mydoc:
    if int(x["file_date"]) <= 20230325:
        myquery2 = {"file_username": x["file_username"],
                    "file_date": x["file_date"]}
        mydoc2 = col2.find(myquery2)
        for i in mydoc2:
            print(i)


# 3. What work done on hpsans13 on date 3-26-2023
print("What work done on hpsans13 on date 3-26-2023:")

myquery = {"file_date": "20230326"}

mydoc = col2.find(myquery)

for x in mydoc:
    print(x)

# 4. Name of all Autodesk Flame users
print("Name of all Autodesk Flame users: ")

myquery = {"machine": "Flame"}

mydoc = col1.find(myquery)

for x in mydoc:
    print(x)
