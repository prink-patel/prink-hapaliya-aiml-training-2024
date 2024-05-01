from pymongo import MongoClient
import logging
logger = logging.getLogger("smart_system")

class DBManager:
    def __init__(self) -> None:
        try:
            self.myclient = MongoClient('mongodb://localhost:27017')
            self.mydb = self.myclient['mydatabase']
        except:
            logger.critical(f"Database not coonected")
        
    # enter values in database
    def enter(self,name,data):
        self.mycollection = self.mydb[name]
        self.mycollection.insert_one(data)



