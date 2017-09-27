# STEP1. receive the numbers from users
def user_input_size():
	size = input("Enter the row and column: ")
	# Alert : if user enter wrong format, ask them to input again
	try:
		size = size.split("*")
		for i in size:
			int(i)
		return size
	except:
		print ("Please Enter 2 numbers(ex: 2*3) !!")
		user_input_size()

# STEP2. Construct the Array and let user to input the elements
def user_enter_elements():
# Announce the list
	inner_array = []
	array = []
# Use 2 for loop to construct the structure
# 2-1 Create the Row
	size = user_input_size()
	for i in range (int(size[0])):
		print ("Row", i+1)
		array.append([])
		# 2-2 Create the columns in each Row
		for j in range (int(size[1])):
			print("(",i ,",",j,")", end=" ")
			array[i].append(input("Input the element: "))
	print (array)
	
# MAIN PROGRAM
user_enter_elements()

#print (array)
# generate the array