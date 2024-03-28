from json_dic import *
from managers.VideoManager import *
from constants import *
class app:
    
    def json(self,url_json):
        self.url_json=url_json
        json_class=json_dic()
        self.sort_json_dic=json_class.run(self.url_json)
        
        
    def run(self,url_video):
        self.url=url_video
        
        videomanager=VideoManager(self.url,self.sort_json_dic)
        videomanager.run()
        
        
    
        
        
app=app()

app.json(json_path)
app.run(url_video)