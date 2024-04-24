email='sindhu@123'
def withdraw(account,amount):
    if amount>account['balance']:
        print('Insufficient funds')
    else:
        uemail=input("Enter the email")
        if email==uemail:
            print('Eligible for withdrawal')
            account['balance']-=amount
            account['transactions'].append(f'Withdrawal:${amount}')
            print(f"Withdrawal successful.Remaining balance:${account['balance']}")
        else:
            print('Not eligible')

def deposit(account,amount):
    uemail=input('Enter the email')
    if email==uemail:
        account['balance']+=amount
        account['transactions'].append(f'Deposit:${amount}')
        print(f'deposit successful.Remaining balance:${account["balance"]}')
    else:
        print('Not eligible')
def get_balance(account):
    return account['balance']
def get_transaction_history(account):
    return account['transactions']
account={
  'balance':1000,
'transactions':[]
    }
choices={
    '1':deposit,
    '2':withdraw,
    '3':get_balance,
    '4':get_transaction_history,
    
    }
while True:
    print('1.Deposit')
    print('2.Withdraw')
    print('3.Check Balance')
    print('4.Transaction history')
    print('5.Exit')
    choice=input('Enter ur choice')
    if choice=='5':
        print('Exiting program')
    if choice in choices:
        if choice=='1' or choice=='2':
            amount=float(input('Enter amount:'))
            choices[choice](account,amount)
        else:
            print(choices[choice](account))
    else:
         print('try again')

            


