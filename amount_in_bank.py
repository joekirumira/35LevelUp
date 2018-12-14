def balance_in_bank():
    amount_in_bank = 500
    new_amount_in_bank = 500+0
    transact = input("Enter key and value separated by commas (,): ")
    transaction, amount = transact.split(",")
    # print(key)
    # print(value)
    amount = int(amount)
    if transaction.lower() == "d":
        amount_in_bank += amount
        new_amount_in_bank = amount_in_bank
    elif transaction.lower() == "w":
        amount_in_bank -= amount
        new_amount_in_bank = amount_in_bank
    else:
        if amount_in_bank <= 0:
            print("You have reached your minimum balance")

    return new_amount_in_bank


if __name__ == "__main__":
    print(balance_in_bank())