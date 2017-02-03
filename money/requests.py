import requests as re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *


DB_NAME = 'sqlite:///hackFMI'

Base = declarative_base()

class Hack(Base):

	__tablename__ = 'Teams'
	id = (Integer, primary_key = True)
	team_name = (String(255), nullable = False)
	team_tehnology = Column(String(255), ForeignKey('tehnologys.id'))

	__tablename__ = 'tehnologys'
	id = (Integer, primary_key = True)
	name = Column(String(255), nullable = False)	

	__tablename__ = 'Rooms'
	id = Column (Integer, primary_key = True)
	room = Column(integer, nullable = False)
	tehnology = Column(String(255), ForeignKey('Teams.id'))

engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
b = Hack()