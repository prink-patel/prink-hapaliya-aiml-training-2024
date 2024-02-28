class truck_object:
    def __init__(self,truck_id) -> None:
        self.truck_id=truck_id
        self.count=0
    
    def count_reset(self):
        self.count=0
    def count_add(self):
        self.count=self.count+1
    def check_count(self,max_number=50):
        if self.count > max_number:
            return True
        else:
            return False