import base64
from pymongo import MongoClient 

print("Enter VM you want to upload")
pushedVM = input()
pushedVM = pushedVM + ".vmdk"

with open("pushedVM", "rb") as image_file:
	encoded_string = base64.b64encode(image_file.read())

client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test?retryWrites=true&w=majority") 
db = client.AMEDScreenShots

#Would need to change this bit to accept input from the GUI
print("Please name this image")
imgName = input()

imgStore = {"name": imgName, "VM": encoded_string}

db.CuckooScreenShots.insert_one(imgStore)
