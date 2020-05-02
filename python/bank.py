'''a simple banking system program'''

class Bank():
    '''A Simple Banking System'''
    def __init__(self,fname,account_num,deposit=0):
        self.user_name = fname.title()
        self.account_number = account_num
        # implicit attributes
        self.balance = deposit
        self.email = 'N/A'
        self.telephone ='N/A'
    
    
    def check_balance(self):
        '''check user's balance'''
        return self.balance

    def deposit(self,amount):
        '''deposit x amount'''
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        '''withdraw some money'''
        if self.balance - amount < 0:
            print(f'Insufficent Funds')
        else:
            print(f'You withdrew {self.balance} from {self.account_number}')


    def profile_info(self):
        return f'''
Account Number: {self.account_number}
=======================
Name: {self.user_name}
Primary Telephone: {self.telephone}
Email: {self.email} \n'''



class Chequing(Bank):
    """ A simple chequing account"""

    def __init__(self,fname,account_num,chequing_account_number,deposit=0):
        #pass instance args to parent constructor
        super().__init__(fname,account_num,deposit) 

        # attributes unique to the child class Chequing
        self.cheq_acc_num = chequing_account_number
        self.service_monthly_charge = 'basic'
        self.transaction_number_limit = 6

        # methods
        # overriding an inherited method
    def check_balance(self):
        if self.service_monthly_charge == 'basic':
            if self.balance < 2000:
                self.balance -= 5.99
                return self.balance
            else:
                return self.balance


