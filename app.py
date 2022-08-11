from flask import Flask, request
from Classes.Queens import Queens
from Classes.Solutions import Solution

app = Flask(__name__)

@app.route('/')

def start():
    n = request.args.get("n", default=8, type=int)
    for N in range(8,n):
        Solution(N).record()
    return "Results store on Database", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
