from factorial import factorial
import json

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    assert factorial(5) == 120

results = {
    "tests": [
        {
            "name": "test_factorial_zero",
            "passed": True
        },
        {
            "name": "test_factorial_one",
            "passed": True
        },
        {
            "name": "test_factorial_five",
            "passed": True
        }
    ]
}

for test in results["tests"]:
    try:
        eval(test["name"] + "()")
    except AssertionError:
        test["passed"] = False

print(json.dumps(results))

