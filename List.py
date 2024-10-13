# Find all records
from mongoConnection import collection
all_records = collection.find()

# Print each record
for record in all_records:
    print(record)
