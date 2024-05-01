from pymongo import MongoClient
import logging

logger = logging.getLogger("smart_system")


class Database:
    def __init__(self) -> None:
        try:
            self.myclient = MongoClient("mongodb://localhost:27017")
            self.mydb = self.myclient["mydatabase"]
            self.mycollection = self.mydb["live_stream_data"]
        except:
            logger.critical(f"Database not coonected")

    # enter values in database
    def enter(self, data):
        print("inside enter")
        self.mycollection.insert_one(data)
        print("data entered")
