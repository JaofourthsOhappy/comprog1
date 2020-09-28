from OO_error import AccountNotFound, InsufficientFund

class BankAccount:

    __account_database = []
    class_name = "BankAccount"
 
    def __init__(self, num, type, name, init_balance):
        self.account_number = num
        self.type = type
        self.account_name = name
        self.balance = init_balance
        self.__account_database.append(self)

    def search_account_db(self):
        for i in range(len(self.__account_database)):
            if self.__account_database[i].account_number == self.account_number :
                return i
        raise AccountNotFound

    def remove(self):
        try : 
            index = self.search_account_db()
        except AccountNotFound:
            print(self.account_number, "account is invalid; nothing to be deleted.")
        else:
            del self.__account_database[index]
    def deposit(self, amount):
        try:
            self.search_account_db()
            self.balance += amount
        except AccountNotFound:
            print(self.account_number , "account is invalid; no witdrawal action performed.")            
    def witdraw(self, amount):
        try:
            self.search_account_db()
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise InsufficientFund
        except AccountNotFound:
            print(self.account_number , "account is invalid; no witdrawal action performed.")
        except InsufficientFund:
            print(amount, "witdrawal amount exceeds the balance of", self.balance, "for", self.account_number, "account.")

    def show_account(self):
        try:
             self.search_account_db()
             print(f'{self.account_number}  {self.type}   {self.account_name}   {self.balance}')
        except AccountNotFound :
            print(self.account_number, "account is invalid; nothing to be shown for.")

    @classmethod    
    def show_all(cls):
        print("List all accounts:")
        for acc in cls.__account_database:
            print(acc.account_number, acc.type, acc.account_name, acc.balance)


