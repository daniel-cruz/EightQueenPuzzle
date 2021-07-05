import pytest
from Classes.Queens import *
import requests


def getAnswersOnline(n):
    try:
        r = requests.get(os.environ["SOLUTIONS_URI"])
        sol_dict = {}
        solutions = str(r.content).split("\\n")
        for solution in solutions:
            try:
                temp = solution.split(" ")
                sol_dict[int(temp[0])] = int(temp[1])
            except:
                print("")
        return sol_dict[n]
    except Exception as e:
        return {}


@pytest.mark.parametrize("n", [8, 9, 10, 11, 12])
def test_number_solutions(n):
    assert Queens(n).solutions == getAnswersOnline(n)
