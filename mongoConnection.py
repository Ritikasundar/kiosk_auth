# mongoConnection.py

from pymongo import MongoClient

# Replace <username>, <password>, and <your-cluster-url> with your actual details
client = MongoClient("mongodb+srv://ritika:ritika23@cluster0.ethop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Create a new database
db = client["kiosk"]  # Replace 'your_database_name' with your actual database name

# Create a new collection
collection = db["menu"]  # Replace 'your_collection_name' with your actual collection name

print("Connected to MongoDB!")
