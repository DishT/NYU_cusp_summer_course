def count_account():
    account_acts = []
    #1.let user enter and read the data
    while len(word) > 0:
        word = input("Enter the Deposit or Withdraw D/W $$$: ")
        account_acts.append(word) 	
    #2.transfer word to math
    
    #3.print out the Ans

# Input Function: User can input their action, until they enter space
def user_enter():
    word = "0"
    while len(word) > 0:
            word = input("Enter D/W $$$: ")
            if len(word) >0:
                account_acts.append(word)   
    return account_acts
# Check each list item and transfer to math
def count_bank_balance(account_acts):
    sum = 0
    for i in range(len(account_acts)):
        account_acts[i] = account_acts[i].split()
        #print (account_acts[i])
        if account_acts[i][0] == "D" :
            sum = sum + int(account_acts[i][1])

        elif account_acts[i][0] == "W":
            sum = sum - int(account_acts[i][1])

        else:
            continue
    return sum

account_acts = []
# STEP1. Let the user enter the D/W 
account_acts = user_enter()
# STEP2. Count the balance
sum = count_bank_balance(account_acts)
# STPP3. Print out the result
print ("Your Bank Balance is $ ",sum)