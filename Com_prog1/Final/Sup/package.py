class Package :
    def __init__(self , packege_id = 0 , from_office = 0, to_office = 0, loaction =0,status =0):
        self.packege_id = packege_id
        self.from_office = from_office
        self.to_office =to_office
       
        if status <= 1:
            self.status = "to mail"
            self.location = self.from_office
        elif status == 2 :
            self.status = "on the way"
            self.location = self.from_office
        elif status == 3:
            self.status = "delivered"
            self.location = self.to_office
    def __str__(self):
        return f"packege id: {self.packege_id} , from: {self.from_office} , to: {self.to_office} , current: {self.location} , status: {self.status}"

    @property 
    def id(self):
        return self.packege_id
    @id.setter
    def id(self,value):
        self.packege_id = value
    @property 
    def f_office(self):
        return self.from_office 
    @f_office.setter
    def f_office(self,value):
        self.from_office = value
    
    @property
    def statuss(self):
        return self.status
    @statuss.setter
    def statuss(self,value):
        self.status = value
    
    @property 
    def t_office(self):
        return self.to_office 
    @t_office.setter
    def t_office(self,value):
        self.to_office = value
