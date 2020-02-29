import base64
from pymongo import MongoClient 
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://BWR:benji@adventurermart-j760a.mongodb.net/test?retryWrites=true&w=majority") 
db = client.AMEDScreenShots

data = db["CuckooScreenShots"]

for x in data.find():
	print(x['name'])

#replace for GUI functionalities
print("Input VM name you want")
imgName = input()

encodedImg = data.find_one({'name': imgName})
newImg = encodedImg["VM"]

#replace for GUI functionalities
print("Input name to save")
saveName = input()
saveName = saveName + ".vmdk"

with open(saveName, "wb") as decoded_image:
	decoded_image.write(base64.decodebytes(newImg))
