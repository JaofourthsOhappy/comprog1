#level1
class Subject():
    def __init__(self,code = 0 ,name ="" , credit = 0):
        self.__code = code
        self.__name = name 
        self.__credit = credit
    def __str__(self):
        return f"{self.__code}, {self.__name}, {self.__credit}"
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,value):
        self.__code = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,value):
        self.__credit = credit



class Student:
    def __init__(self,name=""):
        self.__name = name
        self.__list_sub = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    def add(self,subject):
        self.__list_sub.append(subject)

#level2
class Subject():
    def __init__(self,code = 0 ,name ="" , credit = 0):
        self.__code = code
        self.__name = name 
        self.__credit = credit
    def __str__(self):
        return f"{self.__code}, {self.__name}, {self.__credit}"
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,value):
        self.__code = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,value):
        self.__credit = credit



class Student:
    def __init__(self,name=""):
        self.__name = name
        self.__list_sub = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    def add(self,subject):
        self.__list_sub.append(subject)
    def drop(self,subject):
        for i in range(len(self.__list_sub)):
            if self.__list_sub[i] == subject:
                self.__list_sub.pop(i)
        
    def show(self):
        print(self.__name)
        for sub in self.__list_sub:
            print(sub)

# Network = Subject("01214211", "" , 2)
# Database = Subject("01211222","Database",3)
# Law = Subject("01211333","Law",1)
# Network.name = "Network"
# print(Network.name)
# JJ = Student("JJ")
# AA = Student("AA")
# print(AA.name)
# JJ.add(Network)
# JJ.add(Law)
# JJ.show()
# AA.add(Database)
# AA.show()
# AA.drop(Database)
# AA.show()

#level3
class Subject():
    def __init__(self,code = 0 ,name ="" , credit = 0):
        self.__code = code
        self.__name = name 
        self.__credit = credit
    def __str__(self):
        return f"{self.__code}, {self.__name}, {self.__credit}"
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,value):
        self.__code = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,value):
        self.__credit = credit



class Student:
    def __init__(self,name=""):
        self.__name = name
        self.__list_sub = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    def add(self,subject):
        self.__list_sub.append(subject)
    def drop(self,subject):
        for i in range(len(self.__list_sub)):
            if self.__list_sub[i] == subject:
                self.__list_sub.pop(i)
        
    def show(self):
        print(self.__name)
        for sub in self.__list_sub:
            print(sub)

while True:
    student_list =[]
    option = input("(s)tudent, s(u)bject, (q)uit: ")
    if option == 's' :
        s_option = input("(a)dd a student , (s)show students , (b)ack : ")
        while s_option != "b":
            if s_option == "a":
                name = input("Enter a student name: ")
                student = Student(name)
                student_list.append(student.name)
            elif s_option == "s":
                for i in student_list:
                    print(i)
            else:
                print("Incorrect Menu!!")
            s_option = input("(a)dd a student , (s)show students , (b)ack")
    elif option == "u":
        u_option = input("(a)dd a subject, (s)how subjects, (b)ack: ")
        list_subject =[]
        while u_option != "b":
            if u_option == "a":
                code = int(input("Enter the subject code: "))
                name = input("Enter the subject name: ")
                credit = int(input("Enter the subject credit: "))
                subject = Subject(code,name,credit)
                list_subject.append(subject)
            elif u_option == "s":
                for i in list_subject:
                    print(i)
            else:
                print("incorrect Menu")
            u_option = input("(a)dd a subject, (s)how subjects, (b)ack: ")
                
    elif option == "q":
        print("Bye")
        break
    else :
        print("Incorrect Menu")