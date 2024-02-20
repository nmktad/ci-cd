from main import FizzBuzz

def test_fizzbuzz():
    number = 3
    assert FizzBuzz(number) == "Fizz"
    number = 5
    assert FizzBuzz(number) == "Buzz"
    number = 15
    assert FizzBuzz(number) == "FizzBuzz"
