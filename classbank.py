class BankAccount:
    def __init__(self,initial_balance):
        self.balance=initial_balance
        self.transactions=[]
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds')
        else:
            self.balance-=amount
            self.transactions.append(f'Withdrawal:${amount}')
            print(f'Withdraw successful.Remainaing balance:${self.balance}')
    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(f'Deposit:${amount}')
        print(f'Deposit successful.Remainaing balance:${self.balance}')
    def get_balance(self):
        return self.balance
    def get_transactions_history(self):
        return self.transactions
account=BankAccount(1000)
print('Balance:',account.get_balance())
account.deposit(500)
account.withdraw(100)
account.withdraw(300)
print('Balance:',account.get_balance())
print('Transactions history:',account.get_transactions_history())