import random


def roll():
    return random.randint(1, 6)


def compare(rolls):
    h, c = rolls
    return h - c


def prompt():
    return input("Roll again?: ")


def play_turn(human_score, computer_score):
    turn = (roll(), roll())
    result = compare(turn)

    print(f'You got {turn[0]} vs. {turn[1]}.')

    if result > 0:
        print("Human wins.")
        human_score += 3
    elif result < 0:
        print("Computer wins.")
        computer_score += 3
    else:
        print("Tie.")
        human_score += 1
        computer_score += 1

    return human_score, computer_score


def start():
    human_score = computer_score = 0
    cont = 'yes'

    while cont not in ('e', 'exit'):
        if cont in ('y', 'yes'):
            human_score, computer_score = play_turn(human_score, computer_score)
        else:
            print("Invalid input, only '(y)es' and '(e)xit are allowed.")
        cont = prompt()

    print(f"""
-----------------------
|      Game Over      |
-----------------------
|  Human   | Computer |
-----------------------
| {str(human_score).center(8, " ")} | {str(computer_score).center(8, " ")} |
-----------------------
    """)


start()
