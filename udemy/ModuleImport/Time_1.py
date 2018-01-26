import time

# time.timezone gives no of seconds offset
# if time.daylight is non zero then rely on time.tzname tuples second string
print(time.timezone, "---", time.tzname, "----", time.daylight)

print("Epoch starts at:" + time.strftime("%c", time.gmtime(0)))

print("Timezone is  {} with offset of {}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\t DST in effect")
    print("\t DST is :" + time.tzname[1])

print("Local Time is " + time.strftime("%Y-%m-%d %H:%M:%S %z %Z", time.localtime()))
print("UTC Time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
