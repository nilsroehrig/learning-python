MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        bet = input(f"What would you like to bet on each line (${MIN_BET}-${MAX_BET})? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You cannot bet ${total_bet}, because it exceeds your balance of ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${bet * lines}.")


main()
