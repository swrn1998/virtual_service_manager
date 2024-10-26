from pymongo import MongoClient
from app.config import Config

# Set up the MongoDB connection
client = MongoClient(Config.MONGO_URI, tls=True, tlsAllowInvalidCertificates=False)
db = client[Config.DATABASE_NAME]
collection = db['api_requests']

# Ensure unique index on 'url' and 'method'
collection.create_index([('url', 1), ('method', 1)], unique=True)
