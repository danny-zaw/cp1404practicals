"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car("TestCar")
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert statements to show if Car sets the fuel correctly
    car = Car("TestCar", fuel=10)
    assert car.fuel == 10, "Car's fuel does not equal 10"

    car = Car("TestCar")
    assert car.fuel == 0, "Car does not set fuel correctly"

run_tests()

doctest.testmod()

def format_phrase(phrase):
    phrase = phrase.strip()
    formatted_sentence = phrase[0].upper() + phrase[1:].lower()

    if not formatted_sentence.endswith("."):
        formatted_sentence += "."
    return formatted_sentence

def test_format_phrase():
    assert format_phrase("hello") == "Hello.", "Format phrase did not function as intended."
    assert format_phrase("It is an ex parrot.") == "It is an ex parrot.", "Format phrase did not function as intended."
    assert format_phrase("i LiKe PizZaS") == "I like pizzas.", "Format phrase did not function as intended."

test_format_phrase()