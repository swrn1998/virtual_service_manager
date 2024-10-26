import os

class Config:
    # MongoDB URI, ideally set as an environment variable
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://cse4nick:UIhunxMwCXOH5mCk@service-virtualization.ca3wg.mongodb.net/?retryWrites=true&w=majority&appName=service-virtualization')
    DATABASE_NAME = 'service-virtualization'
