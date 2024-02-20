def FizzBuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

def main():
    input_number = int(input())
    print(FizzBuzz(input_number))  

if __name__ == "__main__":
    main()
