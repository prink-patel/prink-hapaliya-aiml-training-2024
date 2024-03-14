from pymongo import MongoClient

class DBManager:
    def __init__(self) -> None:
        

        self.myclient = MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient['mydatabase']
    def enter(self,name,data):
        self.mycollection = self.mydb[name]
        self.mycollection.insert_one(data)


