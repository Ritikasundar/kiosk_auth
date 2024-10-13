# Define the query
from mongoConnection import collection
query = {"name": "poori"}

# Delete the record
collection.delete_one(query)
print("Record deleted!")
