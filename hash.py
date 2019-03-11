import hashlib

print("\n")
print("---------- MogHunter/hashProgram MD5 Digest V.0 ----------\n")


def hashpassMD5(clear_password):
	hashed_password = hashlib.md5(clear_password).hexdigest()
	print("--------------------- Your Hash ----------------------\n")
	print("password: " + str(clear_password))
	print("hash: " + str(hashed_password))
	print("\n-------------------- End Script --------------------\n")
	return 


def hashpassSHA_1(clear_password):
	hashed_password = hashlib.sha1(clear_password).hexdigest()
	print("--------------------- Your Hash ----------------------\n")
	print("password: " + str(clear_password))
	print("hash: " + str(hashed_password))
	print("\n-------------------- End Script --------------------\n")
	return 

	

init = True
while init  == True:
	choice = input("\nVoulez-vous hasher un mot de passe ?\n1.MD5 \n2.SHA-1\nVotre choix: ")
	if choice == "1":
		my_password = input("Entrez le mots de passe a hasher: ").encode() 
		print("\n")
		if my_password != b"":
			hashpassMD5(my_password)
	elif choice != "1" and choice != "2":
		print("Nous n'avons pas compris votre choix")	
		break		
	elif choice == "2":
		my_password = input("Entrez le mots de passe a hasher: ").encode() 
		print("\n")
		if my_password != b"":
			hashpassSHA_1(my_password)
init = False


