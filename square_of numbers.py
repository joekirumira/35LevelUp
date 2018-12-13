
def square_numbers():
    numbers = list(range(1, 21))
    square = []
    for num in numbers:
        square.append(num**2)

    return square[0:5]


if __name__ == "__main__":
    print(square_numbers())