fizzbuzz = []


def generate():
    for number in range(1, 101):
        if number % 15 == 0:
            fizzbuzz.append("FizzBuzz")
        elif number % 3 == 0:
            fizzbuzz.append("Fizz")
        elif number % 5 == 0:
            fizzbuzz.append("Buzz")
        else:
            fizzbuzz.append(number)


def printFB():
    generate()

    # Print out the move list in formatted columns for readability
    colCount = 0
    for item in fizzbuzz:
        if colCount == 0:
            print("\t", end="")
        print("{:<10}".format(item), end="")
        colCount += 1

        if colCount == 10:
            print()
            colCount = 0


if __name__ == "__main__":
    printFB()
