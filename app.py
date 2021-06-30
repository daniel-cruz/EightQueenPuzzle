from flask import Flask
from Classes.Queens import Queens
import datetime

app = Flask(__name__)

@app.route('/')

def start():
	print(datetime.datetime.now().strftime("%X"))
	for N in range(8,13):
		Queens(N)
	print(datetime.datetime.now().strftime("%X"))
	return "See on terminal"

	start()

