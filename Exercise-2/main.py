import time

# Get current hour as integer
hour = int(time.strftime('%H'))

print("Current Time:", time.strftime('%H:%M:%S'))

if 0 <= hour < 12:
    print("Good Morning Sir!")
elif 12 <= hour < 17:
    print("Good Afternoon Sir!")
elif 17 <= hour < 21:
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
