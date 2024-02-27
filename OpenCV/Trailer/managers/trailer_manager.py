import json


class trailer_manager:
    def __init__(self,i) -> None:
        self.i=i
        self.json_path=f"/home/wot-prink/Desktop/hello/OpenCV/Trailer/trailer_entries-65dc30a819989/MRKDC_0984_0{self.i}__01_13_2024_05_59_03_500_AM_UTC-05_00_01132024.json"
        
    def Values_trai(self):
        
        self.f = open(self.json_path)
        data = json.load(self.f)
        dic={}
        print("trailer_manager")
        for idx in range(len(data["messages"])):
            
            for idy in range(len(data["messages"][idx]["objects"])):
                
                if data["messages"][idx]["objects"][idy].split("|")[0] == "TOP":
                    object_data = data["messages"][idx]["objects"][idy].split("|")
                    triler_id = object_data[1]
                    ts=data["messages"][idx]['ts']
                    x1=object_data[3]
                    y1=object_data[4]
                    x2=object_data[5]
                    y2=object_data[6]
                    id=data["messages"][idx]["id"]
                    dic[triler_id]=[x1,y1,x2,y2,ts,id]
        print("end trailer")
        return dic          
                