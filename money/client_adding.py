from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from module import *

Session = sessionmaker(bind = engine)
session = Session()


class Adding_Clients(BankUser):


	session.add_all([
	BankUser(username = "Rado", password = '123', balance = 512, message = 'Ok'),
 	BankUser(username = "Roza", password = 'weiodjwe', balance = 9999, message = 'Roza e qka'),
	BankUser(username = "Ivan", password = 'weiodjwe', balance = 5243, message = 'Oke')])
	
	session.commit()
