import sqlite3

class main_menu:

	def __init__(self, choice, user):
		self.database = sqlite3.connect(db_name)
		self.choice = input('>')
		self.user = None


	def is_logged(self):
		return self.user is not None

	def log_in(self):
		if self.user is not None:
			print('Logged as {username}. Wanna Log out? y/n'.format(
								username = self.user[TAKE_USER_NAME]))
		if choice == 'y' or 'Y':
			return
		self.user = None

	def show_movie(self):
		if choice == 'show movies':
			print('Current movies are: ')
			self.database.execute(SHOW_MOVIES_BY_ID)

	def make_reservation(self):
		if choice == 'make reservation':
			pass
	
def main():
	pass
if __name__ == '__main__':
	main()
