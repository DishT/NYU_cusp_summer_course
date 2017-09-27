import csv
import pandas as pd
import datetime as dt


# create/reset a csv file with an empty dataframe
with open('todo.csv', 'w') as f:
    df = pd.DataFrame(columns = ['Timestamp', 'Task', 'Priority'])
    df.to_csv('todo.csv')

    
# define user functions
def addTask(task, prior = 3):
    """
    Args:
        task (str): task description
        prior (int, optional): set priority from 1 to 3 with default being the lowest (3)
    Returns:
        updated todo.csv with the given new task
    """
    # setup data
    time = dt.datetime.now()
    data = {'Timestamp': time,
            'Task': str(task),
            'Priority': str(prior)}
    
    # append task and save
    df = openFile()
    df = df.append([data], ignore_index=True)
    df = saveFile(df)

def delTask(index):
    """
    Args:
        index (int): task index of the task to be deleted
    Returns:
        updated todo.csv with specified task removed
    """
    # remove task and save
    df = openFile()
    df = df[df.index != index]
    df = saveFile(df)

def viewTask(sort = 'Timestamp'):
    """
    Args:
        sort (str): column name for sorting, default being 'Timestamp'
                    (creation time of tasks)
    Returns:
        a printed list with tasks being sorted and re-indexed accordingly
    """
    # sort task and print
    df = openFile()
    df = df.sort_values(by = sort)
    df = saveFile(df)
    
    print('Tasks:')
    for i in df.index:
        print('{I}. {T} (priority: {P})'
              .format(I = i, T = df.loc[i, 'Task'], P = df.loc[i, 'Priority']))
    print('\n')


# define back-end functions
def openFile():
    df = pd.read_csv('todo.csv', index_col = 0)
    return(df)

def saveFile(df):
    """re-index given df starting from 1, then write df into csv"""
    df = df.reset_index(drop=True)
    df.index += 1
    df.index.name = 'Index'
    df.to_csv('todo.csv')
    return(df)


# test
print('Add new tasks')
addTask('Take dog for a walk')
addTask('Submit Challenge 3 solutions', 1)
viewTask()

print('Remove task 1')
delTask(1)
viewTask()

print('Add new tasks')
addTask('Take dog for a walk')
addTask('Mail letters', 2)
viewTask()

print('Sort according to priority')
viewTask('Priority')

print('Remove task 2')
delTask(2)
viewTask()
