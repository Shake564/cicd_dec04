import sys
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import multiply, add, divide, sub, squareRoot, naturalLog, sin, cos, square

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(3,-4) == -12
    assert multiply(-3,-4) == 12

def test_add():
    assert add(3, 4) == 7
    assert add(7000, 2005146) == 2012146
    assert add(0, 0) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 20) == 0
    assert divide(10000, 10) == 1000

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_sub():
    assert sub(6, 3) == 3
    assert sub(3, 6) == -3

    assert sub(10000, 3) == 9997
    assert sub(3, 10000) == -9997

def test_log():
    assert naturalLog(2.7183) == 1
    assert naturalLog(1) == 0
    assert naturalLog(0) == "Bound Error (Log)"
    assert naturalLog(-1) == "Bound Error (Log)"

def test_square():
    assert square(2) == 4
    assert square(-2) == 4

    assert square(1) == 1
    assert square(-1) == 1

def test_sin():
    assert sin(90) == 1
    assert sin(180) == 0
    assert sin(270) == -1
    assert sin(0) == 0
    assert sin(360) == 0
    assert sin(360000) == 0

def test_cos():
    assert cos(90) == 0
    assert cos(180) == -1
    assert cos(270) == 0
    assert cos(0) == 1
    assert cos(360) == 1
    assert cos(360000) == 1

def test_squareRoot():
    assert squareRoot(4) == 2
    assert squareRoot(1) == 1
    assert squareRoot(0) == 0

    assert squareRoot(-1) == "Negative sqrt error"

def test_percent():
    assert percent(200, 10) == 20
    assert percent(100, 5) == 5
    assert percent(789, 0) == 0
    assert percent(10, 200) == 20