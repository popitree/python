# UTC = Coordinated Universal Time
# ZULU Time
import time
import random

print(time.time() / (365*24*60*60))

print(time.gmtime())
# UTC

print(time.localtime())

print(time.localtime(time.time()))

print(time.gmtime(0))

time_here = time.localtime()
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

print("perf_counter: {}".format(time.perf_counter()))
print("monotonic: {}".format(+time.monotonic()))
print("time: {}".format(time.time()))


# This is not a good practice to import from std library like this
from time import monotonic as my_timer

# but now instead of time() function we can use
# perf_counter or monotonic or process_time
# without changing the code below
# process_time is used for profiling (how much time of CPU used)
# perf_counter is best to see elapsed time as in case here

y = random.randint(0, 9)
x = -1
while x != str(y):
    x = input("Press {} enter to start:".format(y))

wait_time = random.randint(1, 6)
time.sleep(wait_time)

start_time = my_timer()
input("Press Enter ro end")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Reaction time {} seconds".format(end_time - start_time))

for clock in ['clock', 'time', 'monotonic', 'perf_counter', 'process_time']:
    print(clock + "():\t\t\t", time.get_clock_info(clock))



