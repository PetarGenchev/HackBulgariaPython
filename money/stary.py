from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_NAME
from sqlalchemy import *
from module import *
import getpass

Session = sessionmaker(bind = engine)
session = Session()

class Bank(BankUser):

    def __init__(self):
        self._user = ""
    def login(self):
    
        print('Enter Username: ')
        self.temp_username = input('>')
        print('Enter Password: ')
        self.temp_password = getpass.getpass('>')
        for user, password in session.query(BankUser.username, BankUser.password).all():
            if self.temp_username in user:
                if password == self.temp_password:
                    self._user = user
                    print('Wellcome you log in as: {}'.format(user))
                    return self.user_choice()
                else:
                    print('Wrong Password!')
                    return login()

    def user_choice(self):
        old_balance = session.query(BankUser.balance).filter(BankUser.username == self._user).first()[0]
        print('Logged deposit or withdraw')
        self.choice = input('>')
        if self.choice == 'deposit':
            amount = input('Enter Amount: ')
            print(self._user)
            new_balance = float(amount) + old_balance
            session.query(BankUser.balance).filter(BankUser.username == self._user).update({'balance' : new_balance})
            print('Deposit Succesfully amount of: {}. Current balance: {}'.format(amount, new_balance))

        if self.choice == 'withdraw':
            amount = input('Enter amount: ')
            if float(amount) <= old_balance:
                new_balance = old_balance - float(amount)
                session.query(BankUser.balance).filter(BankUser.username == self._user).update({'balance' : new_balance})
                print('Withdraw Succesfully amount of: {}.Current Balace: {}'.format(amount,new_balance))
        session.commit()
        session.close() 
        
B = Bank()
B.login()