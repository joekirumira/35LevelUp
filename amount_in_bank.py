def balance_in_bank():
    amount_in_bank = 500
    new_amount_in_bank = 500+0
    transact = input("Enter key and value separated by commas (,): ")
    key, value = transact.split(",")
    for key in transact:
        if key == D or key == d:
            amount_in_bank += transact[key]
            amount_in_bank = new_amount_in_bank
        elif key == W or key == w:
            amount_in_bank -= transact[key]
            amount_in_bank = new_amount_in_bank
        else:
            if amount_in_bank <= 0:
                print("You have reached your minimum balance")

    return new_amount_in_bank


if __name__ == "__main__":
    print(balance_in_bank())