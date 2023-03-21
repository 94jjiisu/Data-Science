MONGO_URI = "mongodb+srv://jisuuser:jisupass@cluster0.nsgft.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

from pymongo import MongoClient
import certifi 

ca = certifi.where()

print(ca)

# client = MongoClient(MONGO_URI, ca)

# DATABASE = 'myFirstDatabase'

# database = client[DATABASE]

# COLLECTION = 'jisu-collection'

# collection = database[COLLECTION]

# collection.insert_one(document={"hello":"jisu"})