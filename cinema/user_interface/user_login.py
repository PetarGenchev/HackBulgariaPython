from user import *

class user_login:

	def __init__(self):
		self.user = None

	def is_logged(self):
		return self.user is not None

	def log_in(self):
		if self.user is not None:
			print('Logged as {}.'.format(self.user[TAKE_USER_NAME]))
		print('Would you like to stay in y/n')
		user_choice = input()
		if user_choice == 'y' or 'Y':
			self.user = None
		return

		user = log_users()

user_login()
