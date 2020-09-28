class Square :
    def __init__(self, lenght , width):
        self.lenght = lenght
        self.width = width
    def cal_area (self, lenght ,width):
        return lenght * width

# square_2 = Square(3,2)
# print(square_2.lenght)
# print(square_2.width)
# print(type(square_2))

class SavingAccount:
  def __init__(self, balance):
    self.balance = balance
  
  def withdraw(self, amount):
    self.balance -= amount
  
  def deposit(self, amount):
    self.balance += amount

list_acc = []
while len(list_acc) <3 :
    money = int(input("Enter money "))
    acc = SavingAccount(money)
    list_acc.append(acc.balance)
    
print(list_acc)
    # acc1 = SavingAccount(500)
    # acc2 = SavingAccount(500.0)
    # SavingAccount.deposit(acc1, 100)
    # acc2.deposit(100)
    # print(acc1.balance) 
    # print(acc2.balance)
