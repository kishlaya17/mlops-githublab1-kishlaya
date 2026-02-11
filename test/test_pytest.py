from src.calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    combined_operation,
)


def test_add():
    assert add_numbers(4, 2) == 6


def test_subtract():
    assert subtract_numbers(5, 3) == 2


def test_multiply():
    assert multiply_numbers(3, 4) == 12


def test_divide():
    assert divide_numbers(10, 2) == 5


def test_combined():
    assert combined_operation(3, 2) == (5 + 1 + 6)
