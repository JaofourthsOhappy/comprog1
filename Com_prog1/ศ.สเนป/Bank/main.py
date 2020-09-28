import bank_account

print(bank_account.account_database)
# bank_account.show_account('246-44-77534')
# bank_account.deposit('246-44-77534', 5000)
# bank_account.show_account('246-44-77534')
# bank_account.witdraw('246-44-77534', 2500)
# bank_account.show_account('246-44-77534')
# bank_account.witdraw('246-44-77534', 4500)
# bank_account.show_account('246-44-77534')
bank_account.create_account('246-99-34454','saving','kao',20)
bank_account.show_account('246-99-34454')
bank_account.deposit('246-99-34454',4000)
bank_account.show_account('246-99-34454')

print(bank_account.account_database)
bank_account.delete_account('246-99-34454')

