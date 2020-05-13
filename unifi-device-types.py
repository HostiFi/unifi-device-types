from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27117)

#Getting the database instance
db = client['ace']
devices = db['device']
device_types = {}

for device in devices.find():
    try:
        device_types[device["model"]] += 1
    except:
        device_types[device["model"]] = 1
        
print device_types
