# insertRecord.py
from mongoConnection import collection  # Import the collection from mongoConnection.py

# Define the record you want to insert
record = {
    "name": "dosai", "description": "cripy", "cost": 60.00
}

# Insert the record into the collection
collection.insert_one(record)

print("Record inserted successfully!")

