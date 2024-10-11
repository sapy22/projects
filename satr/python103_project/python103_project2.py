from datetime import datetime


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def is_enough_balance(self,amount):
        if amount > self.get_balance():
            return False
        return True

    def datetime_now(self):
        date = datetime.today()
        return date.strftime('%A, %Y %B %d, %I:%M %p')


# main program
acc1 = BankAccount()
while True:
    print('')
    print('########################## welcome to bank account managment system ####################################')
    print('### type (b) to get your current balance, (d) to deposit money into your account, (w) to withdraw money from your account, (x) to exit the program ###')
    print('')

    command = input('please input a command: ')
    #
    if command == 'b':
        balance = acc1.get_balance()
        print('')
        print(f'your currnet balance is: {balance} $')
        print('')
    #
    elif command == 'd':
        while True:
            num = input('to deposit money input (1) or (0) to return: ')
            if num == '0':
                break
            elif num == '1':
                amount = input('please input an amount: ')
                try:
                    amount = int(amount)
                    if amount > 0:
                        acc1.deposit(amount)
                        date = acc1.datetime_now()
                        print()
                        print(f'{amount} $ has been deposited into your account on {date}')
                        print()
                    else:
                        print('please input an amount greater than 0')
                except:
                    print('invalid amount')  
    #   
    elif command == 'w':
        while True:
            num = input('to withdraw money input (1) or (0) to return: ')
            if num == '0':
                break
            elif num == '1':
                amount = input('please input an amount: ')
                try:
                    amount = int(amount)
                    if amount > 0:
                        if acc1.is_enough_balance(amount):
                            acc1.withdraw(amount)
                            date = acc1.datetime_now()
                            print()
                            print(f'{amount} $ has been withdrawn from your account on {date}')
                            print()
                        else:
                            print('not enough balance')
                    else:
                        print('please input an amount greater than 0')
                except:
                    print('invalid amount')              
    #           
    elif command == 'x':
        exit()
