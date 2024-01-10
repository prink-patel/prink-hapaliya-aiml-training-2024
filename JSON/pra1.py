import json
class Vehicle:
    def __init__(self,name,engine,price) -> None:
        self.name=name
        self.engine=engine
        self.price=price
v1=Vehicle("he","hehe",2000)

jsonstr1 = json.dumps(v1.__dict__) 
print(jsonstr1)
vehicle1=json.loads(jsonstr1)
print(vehicle1)
