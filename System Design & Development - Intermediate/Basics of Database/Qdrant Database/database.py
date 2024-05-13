import qdrant_client
from qdrant_client import QdrantClient, models
from qdrant_client.models import PointStruct, Distance, VectorParams

class Database:
    def __init__(self):
        self.id=0

    def collection(self):
        """client and collection create
        """
        self.client = QdrantClient(host="localhost", port=6333)
        self.collection = self.select_collection()
        
    def select_collection(self):
        """collection select
        """
        COLLOCTION="he"
        try:
            return self.client.get_collection(COLLOCTION)
        except qdrant_client.http.exceptions.UnexpectedResponse:
            return self.client.create_collection(COLLOCTION,
                                                 vectors_config=VectorParams(size=1024,distance=Distance.COSINE))
        except Exception as e:
            print(e)

    def upsert(self, vectors,filename):
        """insert data

        Args:
            vectors (float): image vectors value from image_embedding.py
            filename (str): image name from image
        """
        self.id=self.id+1
        self.client.upsert("he", points=[PointStruct(id=self.id, vector=vectors,payload={'filename':filename})])