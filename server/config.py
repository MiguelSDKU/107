import pymongo
import certifi 


con_string = "mongodb+srv://MikeCG1:poo00p@cluster0.wq6vwpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_string, tlsCAfile=certifi.where())
db = client.get_database("organika")