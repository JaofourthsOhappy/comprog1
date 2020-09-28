class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age=  age
        self.distance = 0
    
    def walk(self,step):
        self.distance+=step
    
    def punch(self,person):
        print(f"{self.first_name} punch {person.first_name}")
    
    def __str__(self):
        return f"My name is {self.first_name} {self.last_name}, I'm {self.age} years old."
    
    
Nice = Person("Nice","Game",18)
Auu = Person("Auu","Lala",18)
list_people = []
condition = 1
while(condition==1):
    first_name = input("First name: ")
    last_name = input("Lasst name: ")
    age = int(input("Age: "))
    people = Person(first_name,last_name,age)
    list_people.append(people)
    condition = int(input("Condition: "))
# print(list_people)
for people in list_people:
    print(people)