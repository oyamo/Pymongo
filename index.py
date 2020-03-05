#!/bin/python
'''
  first run the mongo-installer.sh 
  make sure the server deamon is running 
  check the status using 
  service mongod status 
  or
  sudo service --status-all | grep postgres
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
'''
  There are two methods that can be used
  -insert_one(..) - Insert the dictionary parameter into the database
  -insert_many(..) - Inserts a lists of dictionaries into the mongo db collection
'''
# Inserting Only one record
random_student = {'Name' : 'Oyamo Brian', 'Age' : 34, 'Course' : 'Computer Science'}
student_details_collection.insert_one(random_student)
# Inserting Many Records
my_friends = [
              {'Name' : 'Peter Joel', 'Age' : 34, 'Course' : 'Computer Science'},
              {'Name' : 'John Doe', 'Age' : 32 'Course' : 'Computer Science'},
                {'Name' : 'Peter Matiko', 'Age' : 32 'Course' : 'Journalism'},
              {'Name' : 'Eric Odinga', 'Age': 54 'Course' : 'Mechanical Engineering'}
            ]
student_details_collection.insert_many(my_friends)

# Reading from Collections
'''
  To select data from a mongodb collection, we use find() and find_one() methods
  - find() - Returns all occurances in the collection
  - find_one() - Returns only one occurance in the collection
  
 '''
all_records = student_details_collection.find()
print(all_records) # Will be printed in a dictionary format

one_record = student_details_collection.find_one()
print(one_record)

# Filtering Collections
'''
  First set a filter eg
  When we want to get all computer Science Students from our collection
  we say;
'''
my_filter = {'Course' : 'Computer Science'}
comp_sci_students =  student_details_collection.find(my_filter)

print(comp_sci_students)

# Deleting Records 
'''
  We use delete_one() and delete_many() methods
  - delete_one() deletes only one instance 
  - delete_many() deletes all instances if the selected records
'''
age32_filter = {'Age': 32}
student_details_collection.delete_many(age32_filter) # Guess What it deletes ; The records of students whose age is 32

# Dropping a collection
'''
  Dropping a collection is deleting a whole collecton and all its records
  we use drop() method
  eg student_details_collection.drop()
'''

              
