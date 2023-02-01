import time

def return_time(time):
    to_min = time / 60
    to_hours = to_min / 60
    to_day =  to_hours / 24

    return to_day

time = return_time(time.time())

print(time)
