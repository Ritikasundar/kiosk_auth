# Define the query
from mongoConnection import collection
query = {"name": "pizza"}

# Find the particular record
particular_record = collection.find_one(query)
print("Particular Record:", particular_record)
