import json
import logging
logger = logging.getLogger("smart_system")

class JsonFile:
    def __init__(self, json_path) :
        
        self.json_path = json_path
        
        try:
            open_json_path = open(self.json_path)
            self.json_datas = json.load(open_json_path)
        except :
            logger.critical(f"invalid json file")
        
    # return camera name desk name and points in dictionary 
    def dic_roi(self):
        json_roi={}
        try:
            for count,json_data in enumerate(self.json_datas):
                key=json_data["key"].split(".")
                points={}
                for box_wise_json_data in json_data["boxes"]:
                    list_point=[]
                    for point in box_wise_json_data["points"]:
                        x=point[0]/json_data["width"]
                        y=point[1]/json_data["height"]
                        list_point.append([x,y])
                    points[box_wise_json_data["label"]]=list_point  
                json_roi[key[0]]=points    
            return json_roi
        except:
            logger.critical(f"json data is invalid")