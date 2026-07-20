#print Current Date and Time.

import datetime as dt
current= dt.datetime.now()
print("Date , Time(hour,minutes,seconds,microseconds.)")
print(current)


# another method :
from datetime import datetime as dt
current= dt.now()
print(current)
#breakdown:
print("Above information breakdown")
print(f'Year: {current.year}, Month:{current.month}, Date:{current.day}')
print(f'hour: {current.hour}, Minutes:{current.minute}, \
Seconds:{current.second}, Microseconds:{current.microsecond}')
