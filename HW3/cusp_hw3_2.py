import math

def formula_volume(r):
	volume = 4/3*(math.pi)*r**3
	return volume

def formula_mass(volume,density):
	mass = volume * density
	return mass

def formula_force(Mass, mass, r):
	weight = ((6.67300 * 10 ** -11)*Mass*mass)/(r**2)
	return weight

def print_out_all_items(weight_result):
for i in range (len (weight_result)):
	print (weight_result[i][0],":",weight_result[i][1])

def users_test_data():
	data_set = [75, 9, ["Mercurry", ]]

weight_result = []
mass = input("weight")
item_numbers = input("How many items to caculate?")

# Main Functions: 
#STEP1. let user to input datas 
#STEP2. caculate each items 
#STEP3. store each items in list
for i in range(int(item_numbers)):
	# STEP1. Input
	target = input("Planet, radius, density").replace(",","").split()
	# STEP2. Caculation
	radius = float(target[1])
	density = float(target[2])

	volume = formula_volume(radius)
	Mass = formula_mass(volume,density)
	# STEP3. Final Caculate & Store in List()
	weight_result.append([target[0], formula_force(Mass, float(mass), radius)])

# STEP4. Print out all items
print_out_all_items(weight_result)
