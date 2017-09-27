# Program Logic :Use the basic function to clarify the password
def checker(password):
	# check each element
	for i in password:
		if i.isdigit():
			dig = 1
		elif i.isupper():
			upper = 1
		elif i.islower():
			low = 1
		elif ("$"in password or "#" in password or "@" in password):
			other = 1
	return (dig + upper + low + other)
# STEP1. user in put
password = input("Please Enter Your password! :")
# STEP2. check Length
if len(password) < 6 or len(password)>12:
	print ("Weak Password")
elif checker(password) == 4:
	print ("Strong Password")
else :
	print ("Weak Password")


