import json


class json_dic:
    def run(self, url_json) -> None:
        self.url_json = url_json
        print("json_class")
        json_sort_dic={}
        json_path = open(self.url_json)
        data = json.load(json_path)
        for i, video in enumerate(data):
            json_sort_dic[video["camera_name"]]=video["rois"]
        return json_sort_dic
