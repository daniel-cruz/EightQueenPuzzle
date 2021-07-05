from flask import Flask, request, url_for, render_template, jsonify
from Classes.Queens import Queens
from Classes.Solutions import Solution
import datetime

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/calculate")
def calculateNQueens():
    n = request.args.get("n", default=8, type=int)
    response = {"code": -1, "message": "Este valor no esta dentro del rango permitido"}
    if 7 < n:
        queen = Solution(n).record()
        response = {
            "code": 0,
            "message": "Se encontraron " + str(queen.solutions) + " soluciones",
            "board": str(queen.display()),
        }

    return jsonify(response), 200


@app.route("/iterate")
def iterateNQueens():
    n = request.args.get("n", default=9, type=int)
    solutions = 0
    if n > 8:
        for n in range(8, n + 1):
            queenN = Solution(n).record()
            # solutions += queenN.solutions

        response = {
            "code": 0,
            "message": "Se encontraron " + str(solutions) + " soluciones",
        }
    else:
        response = {
            "code": -1,
            "message": "Error: el input debe ser mayor a 8 para iterar",
        }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
