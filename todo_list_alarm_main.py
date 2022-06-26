""" 

Project Name: Create a todo list and set time alarm for each of them
Author: Valentina Costin

"""

################
# Libraries
################

import os
import random
import webbrowser
import threading

#################
# Modules
#################
from alarm import ring_alarm

# Check if a txt file for youtube alarm not exist then create one
if not os.path.isfile("alarm_youtube.txt"):
    with open("alarm_youtube.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=VEMFlGJtoEU")

def alarm_user_input_checker(alarm_time):
    ''' 
    Check if the user has entered a valid alarm input 
    The possible format:  [Hour:Minute] or [Hour:Minute:Second] 
    '''

    if len(alarm_time) == 2: 
        #  [Hour:Minute]
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and  alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:
        #  [Hour:Minute:Second] 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and  alarm_time[1] < 60 and alarm_time[1] >= 0 and \
            alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True

    return False

if __name__ == '__main__':
    # map with task description as key and alarm task as value
    todo_map = dict()

    exit_key = input('Do yoy want to add a task in todo list? (y/n) ')
    
    while exit_key != 'n':
        # add task in todo list 
        task = input("Task description: ")

        # set alarm for the current task
        alarm_task = input("Alarm task (Eg: 08:00): ")

        try:
            alarm_time = [int(n) for n in alarm_task.split(":")]

            if alarm_user_input_checker(alarm_time):
                todo_map[task] = alarm_time
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Please, enter time in HH:MM format")
            

        exit_key = input('Do yoy want to add a task in todo list? (y/n) ')

    thread_list = []
    idx = 0

    # for each task call the alarm
    for task in todo_map:
        # create thread name
        thread_alarm_name = "thread_alarm_"+ str(idx)

        # create thread
        thread_alarm_name = threading.Thread(target = ring_alarm, args=(todo_map[task],))

        thread_list.append(thread_alarm_name)
        idx = idx + 1
    
    for th in thread_list:
        th.start() # start the thread

    for th in thread_list:
        th.join() # join the thread
 
    print("Exit todo list app!")