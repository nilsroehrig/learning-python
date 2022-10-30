import random

RULES = {
    "rock": {
        "beats": "scissors",
        "is_beaten_by": "paper"
    },
    "paper": {
        "beats": "rock",
        "is_beaten_by": "scissors"
    },
    "scissors": {
        "beats": "paper",
        "is_beaten_by": "rock"
    }
}

MOVE_MAP = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}


def choose_move():
    print("Available moves: (r)ock | (p)aper | (s)cissors")
    move = input("Choose move: ")
    return MOVE_MAP.get(move.lower(), move.lower())


def choose_random_move():
    return random.choice(('rock', 'paper', 'scissors'))


def calc_winner(human_move, computer_move):
    if RULES[human_move]['is_beaten_by'] == computer_move:
        return 'Computer'
    if RULES[human_move]['beats'] == computer_move:
        return "Human"

    return "Tie"


def calc_score(winner, human_score, computer_score):
    if winner == 'Human':
        return human_score + 3, computer_score

    if winner == 'Computer':
        return human_score, computer_score + 3

    return human_score + 1, computer_score + 1


def start():
    human_move = None
    human_score = 0
    computer_score = 0

    while human_move != 'q':
        human_move = choose_move()
        computer_move = choose_random_move()

        if human_move in ('rock', 'paper', 'scissors'):
            print(f"You chose {human_move}. Computer chose {computer_move}")
            winner = calc_winner(human_move, computer_move)
            human_score, computer_score = calc_score(winner, human_score, computer_score)

            print("Tie.") if winner == 'Tie' else print(f"{winner} wins.")
            print(f'Current Score: Human {human_score} vs. Computer {computer_score}.')

        elif human_move == 'q':
            print('Goodbye.')
        else:
            print("Invalid move.")


start()
