# Store string as List()
def store_data(item):
    to_do_data.append(item)
# Remove the data out of List()
def remove_data(item):
    print("Delete the item", to_do_data[int(item[0])-1])
    print ("Before Delete:")
    view_data()
    to_do_data.remove(to_do_data[int(item[0])-1])
    print ("After Delete:")
    view_data()
# Show all item in the list()
def view_data():
    for i in range(len(to_do_data)):
        print ((i+1),".", to_do_data[i])
# Signals show, if the user type wrong actions.
def alert_message():
    print ("======Alert=======")
    print ("Master, I do not know what u want me to do!")
    print ("Sorry > <, Please Enter Again, I can only do (addTask/viewTask/delTask)")
    AI_helper()
# 4 ways Action for this program
def AI_helper_logic(service_fuction, service_todo):
    if service_fuction == "addTask":
        store_data(service_todo)
    elif service_fuction == "viewTask":
        view_data()
    elif service_fuction == "delTask":
        remove_data(service_todo)
    else:
        alert_message()    


# File Functions : Store and Load
def file_store(to_do_data):
    tmp = ""
    file = open('ToDoList.txt','w')
    for i in range(len(to_do_data)):
        
        tmp = str(to_do_data[i][0])+" "+str(to_do_data[i][1]) + "\n"
        file.write(tmp)
    
    file.close()

def file_load():
    file = open('ToDoList.txt')
    
    for line in file:
        #line = line[:-1]
        to_do_data.append(line.strip().split())
        
    print (to_do_data)
    file.close()

# Main program
def AI_helper():
    service = "starter"
    while len(service) != 0:
        service = input("Master, what r u going to Do? \n 3 Functions: (addTask/viewTask/delTask): ")
        # Check out whether user enter space
        if len(service) == 0:
            print("========Thank You========")
            print("Thank you for using AI-ToDo List!")
            file_store(to_do_data)
            break
        else:
            try:
                service = service.replace(")","").replace("("," ").split()
                # Convert the word to 2 word
                service_fuction = service[0]
                service_todo = service[1:]
                # Main Program logic: seperate to 4 ways
                AI_helper_logic(service_fuction,service_todo)
            except:
                alert_message()
# Custom key function : 
def priority(to_do_data):
    return to_do_data[1]
# Custom sort function :
def sort_by_priority(to_do_data):
    to_do_data_sort = sorted(to_do_data, key = priority)
    print(to_do_data_sort)
# STEP1. Read data

# STEP2. Check the users: Functions

# STEP3. Operate the Actions   

# To do #
#1. Store in the file (Check)
#2. read from the file (Check)
#3. Add the piority and Sorting (Check)

to_do_data = list()
file_load()
AI_helper()
print("Sort by priority:")
sort_by_priority(to_do_data)
