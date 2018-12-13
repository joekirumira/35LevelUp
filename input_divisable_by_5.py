def divisible_by_5():
    divisible = []
    num = list(input("Enter four numbers here:"))
    for number in num:
        if number%5 ==0:
            divisible.append(number)
    return divisible


if __name__ == "__main__":
    print(divisible_by_5())