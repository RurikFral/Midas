import time

# This is used to get a current milisecond time stamp. 
# Note this may not always be accurate due to some computers only reporting time to the nearest second.
def current_milli_time():
    return round(time.time() * 1000)