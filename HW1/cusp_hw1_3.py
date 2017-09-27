def counter(word):
	letter_count = 0
	dig_count = 0
	# Method 2 : dict()

	for i in range (len(word)):
		if word[i].isalpha():
			#Method 1 : counter
			letter_count += 1
			#Method 2 : dict()
			letter_count_dic["Letters"] = letter_count_dic.get("Letters",0)+1
		elif word[i].isdigit():
			# Method 1 : Counter
			dig_count += 1
			# Method 2 : dict()
			dig_count_dic["Digits"] = dig_count_dic.get("Digits", 0) + 1
	sum_up = {"LETTERS":letter_count, "DIGITS": dig_count}
	
	for i in sum_up:
		print (i , sum_up[i])


letter_count_dic = dict()
	
dig_count_dic = dict()
# STEP1. read the string
word = input ("Please Enter: ")
# STEP2. Check the letter and digit
# STEP3. Print out the Anwser
counter(word)
print (letter_count_dic)
	
print (dig_count_dic)

