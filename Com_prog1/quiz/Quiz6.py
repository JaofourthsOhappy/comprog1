# class Car:
#     def __init__(self, brand = "_"  , model = "_" , price = 0):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def __str__ (self):
#         return (f"Brand: {self.brand} , Model: {self.model} , Price: {self.price}")

class Car:
    def __init__(self, brand = "_"  , model = "_" , price = 0):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def __str__ (self):
        return (f"Brand: {self.__brand} , Model: {self.__model} , Price: {self.__price}")
    @property
    def brand(self):
        return (self.__brand)
    @brand.setter
    def brand(self,brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model     
    @model.setter
    def model(self,model):
        self.__model = model

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price = price
        
def compare(car1,car2):
    print(car1)
    print(car2)

car1 = Car()    
print(car1)
print()
car1.brand = "Toyota"
print(car1)
print()
car1.model = "Vios"
car1.price = 500000
print(car1)
print()
car2 = Car("BMW" , "X3" , 3500000)
print(car2)
print()
car2.price = 2000000
print(car2)
print()
car2 = Car("Toyota" , "Vios" , 400000)
car1 = Car("Nissan" , "Tiida" , 450000)
car3 = Car("BMW" , "X3", 340000)
compare(car3,car1)
print()
compare(car1,car2)
print()


"(n)ew Route ,(s)how, (c)hoose ,(q)uit:"
"""
59 Sanamloung Ransit
29 Hualampong Rangsit
"""