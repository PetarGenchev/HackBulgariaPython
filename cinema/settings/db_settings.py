import hashlib
db_name = 'cinema'

def hash_password(password):
	hash_obj = hashlib.sha512(password.encode())
	return hash_obj.hexdigest()
