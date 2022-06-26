""" 

Project Name: Alarm Clock and backup of 10 minutes automatically
Author: Valentina Costin

"""

import datetime
import time

def ring_alarm(alarm_time):
    '''
    This function receives an alarm and will open a random alarm song from the alarm_youtube.txt file
    '''

    # Convert the alarm time to seconds
    seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second

    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

    # Get the current time of day in seconds
    now = datetime.datetime.now()
    current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

    # Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds

    # If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:
        time_diff_seconds += 86400 # number of seconds in a day


    print("Alarm set to go off in %s " % datetime.timedelta(seconds=time_diff_seconds))

    time.sleep(time_diff_seconds)

    print("Wake Up!")

    # Load list of possible video URLs for alarm
    with open("alarm_youtube.txt", "r") as alarm_file:
        videos = alarm_file.readlines()

    # Open a random video from the playlist
    webbrowser.open(random.choice(videos))