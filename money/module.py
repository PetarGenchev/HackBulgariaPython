from settings import DB_NAME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *


Base = declarative_base()

class BankUser(Base):

	__tablename__ = 'client'
	id = Column(Integer, primary_key = True)
	username = Column(String(250), nullable = False)
	password = Column(String(250), nullable = False)
	balance = Column(Float, nullable = False)
	message = Column(String(250), nullable = False)

	def __str__(self):
		return 'Client: {}'.format(self.username)

	def __repr__(self):
		return self.__str__()

	

engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
b = BankUser()
