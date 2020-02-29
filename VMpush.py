import base64
from pymongo import MongoClient 

#Would need to change this bit to accept input from the GUI
print("Enter VM you want to upload")
pushedVM = input()
pushedVM = pushedVM + ".ova"

with open(pushedVM, "rb") as image_file:
	encoded_string = base64.b64encode(image_file.read())

client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test?retryWrites=true&w=majority") 
db = client.AMEDScreenShots



imgStore = {"name": imgName, "VM": encoded_string}

#Eventually change this to different table
db.CuckooScreenShots.insert_one(imgStore)
