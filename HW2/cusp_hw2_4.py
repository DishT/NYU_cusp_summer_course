#Method 1 : Dictionary
#Method 2 : Lists

# Input Function : Let user input the data
def input_data():
	data = input("Input the String: ")
	data = data.lower().replace(",", "").split()
	
	return data
# Histogram Function 1: Implement the histogram by dictionary
def histogram():
	histogram = dict()
	data = input_data()

	for i in data :
		histogram[i] = histogram.get( i , 0) + 1
	return histogram

# Histogram Function 2: Implement the histogram by list
def histogram_list():
    original_data = input_data()
    new_data = []
    # Seperate each word from the original data
    for i in range (len(original_data)):
        if original_data[i] not in new_data:
            new_data.append(original_data[i])
    # Sort the list
    new_data_sort = sorted(new_data)


    # Use count method to count each word
    for i in range (len(new_data_sort)):
        print(new_data_sort[i], original_data.count(new_data_sort[i]))
# Sort Function : sort the dic() by the item()
def sort_by_word(histogram):
	tmp = sorted (histogram.items())
	#print (tmp)
	for k, v in sorted(histogram.items()):
		print (k,v)
# MAIN PROGRAM

# STEP1. Let the user to input the String

# This Fuction included in the "histogram()""

# STEP2. Create the Histogram to count the words
# STEP3. Sort the histogram by word
print ("Method 1 : implement by Dictionary")
sort_by_word(histogram())
print ("Method 2 : implement by List")
histogram_list()

