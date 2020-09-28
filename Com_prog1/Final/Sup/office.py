from package import *
class Office:

    def __init__(self,id :int):
        self.office_id = id
        self.mailin_list = []
        self.mailout_list = []
    def get_office_id(self):
        return self.office_id
    def __str__(self):
        string = f"Officr id {self.office_id}"
        string+= f"\nMail-in Packeges"
        for j in (self.mailin_list):
            string += f"\n{j}"
        string += f"\nMail-out Packeges"
        for i in (self.mailout_list):
            string += f"\n{i}"
        return string
    # fill in your own code
    
    def add_package_to_mailout(self, package):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office101.add_package_to_mailout(pack1)
            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages: 
                packet id: 1, from: 101, to: 102, current: 101, status: to mail
            
        '''
        # fill in your own code
        self.mailout_list.append(package)
    


    def add_package_to_mailin(self, package):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office102 = Office(102)
            >>> office102.add_package_to_mailin(pack1)
            >>> print(office102)
                Office id: 102
                Mail-in Packages: 
                packet id: 1, from: 101, to: 102, current: 101, status: to mail
                Mail-out Packages:

        '''
        # fill in your own code
        self.mailin_list.append(package)
    
    def transfer(self,dest_office):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office102 = Office(102)
            >>> office101.add_package_to_mailout(pack1)
            >>> office101.transfer(office102)
            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages: 
                packet id: 1, from: 101, to: 102, current: 101, status: on the way

        '''
        # fill in your own code
        # dest_office.add_package_to_mailin(self.mailout_list)
        for pack in self.mailout_list:
            if pack.t_office == dest_office.get_office_id():
                pack.status = "on the way"


    def deliver(self, dest_office):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office102 = Office(102)
            >>> office101.add_package_to_mailout(pack1)
            >>> office101.transfer(office102)
            >>> office101.deliver(office102)
            >>> print(office102)
                Office id: 102
                Mail-in Packages: 
                packet id: 1, from: 101, to: 102, current: 102, status: delivered
                Mail-out Packages: 

            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages:
                
        '''        
        # fill in your own code
        for pack in self.mailout_list:
            dest_office.add_package_to_mailin(pack)
        for pack in self.mailout_list:
            pack.status = "delivered"
        self.mailout_list =[]
    def clear(self):
        # fill in your own code
        self.mailin_list = []
        self.mailout_list = []

    ### for level 3
    def deliver2(self, dest_office):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office102 = Office(102)
            >>> office101.add_package_to_mailout(pack1)
            >>> office101.transfer(office102)
            >>> office101.deliver(office102)
            >>> print(office102)
                Office id: 102
                Mail-in Packages: 
                packet id: 1, from: 101, to: 102, current: 102, status: delivered
                Mail-out Packages: 

            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages:
                
        '''
        # fill in your own code
        remain_pack = []
        for pack in self.mailout_list:
            if pack.t_office == dest_office.get_office_id():
                pack.status = "delivered"
            else:
                pack.status = "to mail"
        for i in range(len(self.mailout_list)):
            if self.mailout_list[i].t_office == dest_office.get_office_id():
                dest_office.add_package_to_mailin(self.mailout_list[i])
            else:
                remain_pack.append(self.mailout_list[i])
        self.mailout_list =[]
        for i in remain_pack:
            self.mailout_list.append(i)
        self.mailin_list = []



        
    

    
