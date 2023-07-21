import json

class ogg:
    Id = 1
    def __init__(self, name, addresser, date, quantity = 1, ) -> None:
        self.Name = name
        self.Quantity = quantity
        self.Addresser = addresser
        self.Date = str(date)
    
        
    def __repr__(self):
        return str(self.Name +" "+ str(self.Quantity) +" "+ self.Addresser +" "+ str(self.Date))
    
    def to_json(self):
        return json.dumps(self.__dict__, indent = 4)