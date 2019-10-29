63

class Bank(object):
    
    accountList=[]
    def display(self): #for printing purposes only
        for account in Bank.accountList:
            print ("*********************")
            for k,v in account.options.items():
                print ('{}: {}'.format(k,v))
            print ("*********************")

    def login_validity(self, u, p): #checks for the correct login 
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return True
        return False

    def load_account(self,u, p): #loads current account
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return account #account object
        return None #no object found
    
    
        
class Account(object):
    default_options = {'accountno':None,'acctype': None, \
               'balance': 0, 'fname': None, 'lname': None, 'line1':None, \
                       'line2': None, 'username': None, 'pin': None}
    def __init__(self, **kwargs):
        #part of ILA
        self.options = Account.default_options.copy()
        self.options.update(kwargs)
        Bank.accountList.append(self)

    def __getitem__(self, key): #get an item by key
        return self.options[key]
    
    def __setitem__(self, key, new_value): #set an item by key
        self.options[key] = new_value
        
    def getBalance(self, accno):
        if accno == self['accountno'] :
                return self['balance']
 
    def deposit(self, amount_to_deposit, accno):
        if accno == self['accountno']:
            self['balance']+= float(amount_to_deposit)
        #please see getBalance on how to access an attribute
        #deposits amount_to_deposit to current user

    def summary(self, accno):
        #return full name, address, account type and current balance
        return [self['fname'] + ' ' + self['lname'], self['line1'] + '\n' + self['line2'], self['acctype'], self.getBalance(accno)]


       
class Saving(Account):

    def withdraw(self, amount_to_withdraw, accno):
        withdraw_charge = 2.53 #flat rate to subtract from saving account
        if accno == self['accountno']:
            self['balance']-=(float(amount_to_withdraw) + withdraw_charge)

class Checking(Account):
    
    def withdraw(self, amount_to_withdraw, accno):
        withdraw_charge = 1.00
        if accno == self['accountno']:
            self['balance']-=(float(amount_to_withdraw) + withdraw_charge)
