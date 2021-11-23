from time import time
import datetime


input("[ENTER] to start and stop")

#set the start time at the time the user pressed enter
start_time = time()


input("running... [ENTER] to stop")

#now get the stop time
stop_time = time()

# stop time - start time = time elapsed
elapsed = datetime.timedelta(0, stop_time - start_time)

#print the results
print("Time Elapsed: " + str(elapsed))