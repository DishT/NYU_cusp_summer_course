import math
# Caculation Fuction : Caculation the formula
def formula(D):
	ans = math.sqrt(2*50*D/30)
	return ans
# Input Fuction: let user can input the parameters
def user_input():
	D_numbers = input ("Enter the parameters: ")
	D_numbers = D_numbers.split(",")
	return D_numbers

# MAIN PROGRAM
# STEP1. User input the numbers
D_numbers = user_input()

Q_ans = []
# STEP2. Caculate each number with Formula
for i in D_numbers:
	Q_ans.append(int(formula(int(i))))
	

# STEP3. Print out the caculations
print (Q_ans)
