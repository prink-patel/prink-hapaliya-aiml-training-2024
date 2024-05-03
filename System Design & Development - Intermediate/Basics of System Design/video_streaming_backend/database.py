from pymongo import MongoClient
import logging
logger = logging.getLogger("Streaming_data")

class Database:
    def __init__(self) -> None:
        try:
            logger.info("Database connected")
            self.my_client = MongoClient('mongodb://localhost:27017')
            self.my_db = self.my_client['database']
        except:
            logger.critical(f"Database not connected")
        
    # enter values in database
    def enter(self,name,data):
        """enter values in database

        Args:
            name (str): database name
            data (dict): dictionary values to store bounding box, time, camera id, image path
        """
        try:
            logger.info("Data inserted")
            self.my_collection = self.my_db[name]
            self.my_collection.insert_one(data)
        except:
            logger.critical(f"Data not inserted")