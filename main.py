from Classes.Queens import Queens
import datetime

print(datetime.datetime.now().strftime("%X"))
for N in range(8,12):
	Queens(N)
	print(N)
print(datetime.datetime.now().strftime("%X"))