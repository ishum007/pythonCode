from datetime import datetime
now = datetime.now()
print(now)                      
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute            
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}') 

from datetime import datetime

now = datetime.now()

print("Current Date and Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

# Timestamp
print("Timestamp:", now.timestamp())

from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

print(formatted_date)

from datetime import datetime

date_string = "5 December, 2019"

date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)

from datetime import datetime

now = datetime.now()

new_year = datetime(now.year + 1, 1, 1)

difference = new_year - now

print("Time until New Year:", difference)

from datetime import datetime

start = datetime(1970, 1, 1)

now = datetime.now()

difference = now - start

print("Difference:", difference)