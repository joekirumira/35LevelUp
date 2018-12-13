

def multiples_of_7():
    result = []
    sample_space = range(2000, 3201)
    for number in sample_space:
        if number%7 == 0 and number%5 is not 0:
            result.append(number)
    return result


if __name__ == "__main__":
    print(multiples_of_7())
