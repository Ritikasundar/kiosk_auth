# insertRecord.py
from mongoConnection import collection
records = [
    {"name": "poori", "description": "2 in a set", "cost": 40.00},
    {"name": "pizza", "description": "spicy", "cost": 1200.00}
]

# Insert records into the collection
collection.insert_many(records)
print("Many records inserted!")