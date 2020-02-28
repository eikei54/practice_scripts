import time;
import calendar;


ticks = time.time()
print("Number of ticks since 12:00am,, Janualy 1, 1970:", ticks)

localtime = time.localtime(ticks)
print(localtime)

cal = calendar.month(2020, 2)
print('Here is the calendr:', cal)

