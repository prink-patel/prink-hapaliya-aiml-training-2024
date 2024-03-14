import json


class json_file:
    def __init__(self, json_path) :
        self.json_path = json_path
        print("json") 
        f = open(self.json_path)
        self.data = json.load(f)
    def dic_roi(self):
        
        json_roi={}
        for count,i in enumerate(self.data):
            # print(i)2
            key=i["key"].split(".")
            print(key)
            # print(i["boxes"])
            points={}
            for j in i["boxes"]:
                list_point=[]
                print(j)
                for point in j["points"]:
                    
                    x=point[0]/i["width"]
                    y=point[1]/i["height"]
                    list_point.append([x,y])
                points[j["label"]]=list_point  
            json_roi[key[0]]=points    
                
        
            
            # print(val["boxes"])
            # json_roi[key[0]]=val['boxes'][0]
        return json_roi