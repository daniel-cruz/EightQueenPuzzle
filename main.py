from Classes.Queens import Queens
import datetime

print("Start: " + datetime.datetime.now().strftime("%X"))
for N in range(8,13):
	Queens(N)
print("End: " + datetime.datetime.now().strftime("%X"))