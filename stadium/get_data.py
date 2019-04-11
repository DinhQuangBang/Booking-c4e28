from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@booking-z36ui.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)

stadium_database = client.stadium_database
stadium_collection = stadium_database["stadium_detail"]

