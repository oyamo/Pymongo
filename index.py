#!/bin/python
'''
  first run the mongo-installer.sh 
  make sure the server deamon is running 
  check the status using --- service mongod status
  if it is not running, run --- service mongod start
 '''
 
# Import pymongo

import pymongo

# Create a database client
myclient = pymongo.MongoClient("mongodb://localhost:2968")

# To create a database eg Student Database

mydb = myclient['student'] # This statement also selects the given database if it exists
# to list databases names use the method list_database_names()
print(myclient.list_database_names())

# Creating a new Collection
'''
  Collections are like Tables in a relational database and it stores a collection of records
  To access records, you must go to the specific location where the records were Kept
  Naming conventions may be used when picking a collection name
'''
student_details_collection = mydb['student-details']

# Inserting Records into a collection
