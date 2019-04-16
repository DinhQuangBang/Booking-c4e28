from pymongo import MongoClient
mongo_uri = "mongodb+srv://admin:admin@booking-z36ui.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
form_database = client.submitted_form
form_collection = form_database["form"]
stadium_database = client.stadium_database
stadium_collection = stadium_database["stadium_detail"]
user_database = client.user_database
user_collection = user_database["user_information"]
partnership_register = client.partnership_register
partnership_collection = partnership_register["partnership_register"]
new = {
    "partner_name": "Test",
    "partner_email": "test@test",
    "partner_phone": "0365160194",
    "partner_address": "test dia chi san",
    "partner_note": "ghi chu"
}
partnership_collection.insert_one(new)