import sqlite3
from create_db import * 
from settings.db_settings import *

class CreateDataBase:
	
	def __init__(self):
		self.database = sqlite3.connect(db_name)
		self.cursor = self.database.cursor()

	def drop_tables(self):
		self.cursor.execute(DROP_USER)
		self.cursor.execute(DROP_MOVIES)
		self.cursor.execute(DROP_PROJECTIONS)
		self.cursor.execute(DROP_RESERVATIONS)
		self.database.commit()

	def create_tables(self):
		self.cursor.execute(CREATE_USER)
		self.cursor.execute(CREATE_MOVIES)
		self.cursor.execute(CREATE_PROJECTIONS)
		self.cursor.execute(CREATE_RESERVATIONS)
		self.database.commit()

	def fill_db(self):
		movies = [('The Hunger Games:Catching Fire', 7.9),
				 ('Wrect-it Ralph', 7.8),
				 ('Her', 8.3)]
		self.cursor.executemany(INSERT_MOVIES, movies)
		self.database.commit()

		users = [('Rosi Zlateva', hash_password('A133926#')),
				('Slavayana Monkova', hash_password('#Rosieop')),
				('Rado Georgiev', hash_password('#Shalqla')),
				('Krasimira Badova', hash_password(':D4314211')),
				('Kiril Hristov', hash_password('Muzikanta13]')),
				('Vlado Putin', hash_password('Motherrussia!'))]
		self.cursor.executemany(INSERT_USER, users)
		self.database.commit()

		projections = [('3D', '2014-04-01', '19:10'),
					  ('2D', '2014-04-01', '19:00'),
					  ('4DX', '2014-04-02', '21:00'),
					  ('2D', '2014-04-05', '20:20'),
					  ('3D', '2014-04-02', '22:00'),
					  ('2D', '2014-04-02', '19:30')]
		self.cursor.executemany(INSERT_PROJECTIONS, projections)
		self.database.commit()

		reservations = [(3, 1, 2, 1),
					   (3, 1 ,3, 5),
					   (3, 1, 7, 8),
					   (2, 3, 1, 1),
					   (2, 3, 1, 2),
					   (5, 5, 2, 3),
					   (6, 5, 2, 4)]
		self.cursor.executemany(INSERT_RESERVATIONS, reservations)
		self.database.commit()

	

def main():
	
	db = CreateDataBase()
	db.drop_tables()
	db.create_tables()
	db.fill_db()

if __name__ == '__main__':
	main()
