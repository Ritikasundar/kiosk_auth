# Define the query and the new values
from mongoConnection import collection
query = {"name": "pizza"}
new_values = {"$set": {"cost": 130}}

# Update the record
collection.update_one(query, new_values)
print("Record updated!")
