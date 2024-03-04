
from pymongo import MongoClient

class DBManager:
    def __init__(self) -> None:
        

        self.myclient = MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient['mydatabase']
        self.mycollection = self.mydb["truck"]
    def enter(self,data):
        self.mycollection.insert_one(data)


