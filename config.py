import pymongo
import certifi

con_str = "mongodb+srv://eddiehooks36:gabsterG36@cluster0.jvbhquv.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore_ch34")