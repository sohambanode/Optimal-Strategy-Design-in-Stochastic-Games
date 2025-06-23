import numpy as np

class StrategyA:
    def __init__(self):
        self.my_history = np.array([1, 1])
        self.outcomes = np.array([1, 0])
        self.opponent_history = np.array([1, 1])
        self.score = 1

    def choose_action(self):
        last_result = self.outcomes[-1]

        if last_result == 1:
            if (1 - (self.score / len(self.outcomes))) > (6 / 11):
                return 0  # attack
            else:
                return 2  # defend
        elif last_result == 0.5:
            return 0
        else:
            return 1  # balanced

    def update_after_round(self, my_move, opponent_move, round_result):
        self.my_history = np.append(self.my_history, my_move)
        self.outcomes = np.append(self.outcomes, round_result)
        self.opponent_history = np.append(self.opponent_history, opponent_move)
        self.score += round_result


class StrategyB:
    def __init__(self):
        self.my_history = np.array([1, 1])
        self.outcomes = np.array([0, 1])
        self.opponent_history = np.array([1, 1])
        self.score = 1

    def choose_action(self):
        latest = self.outcomes[-1]
        if latest == 1:
            return 2
        elif latest == 0.5:
            return 1
        else:
            return 0

    def update_after_round(self, my_move, opponent_move, round_result):
        self.my_history = np.append(self.my_history, my_move)
        self.outcomes = np.append(self.outcomes, round_result)
        self.opponent_history = np.append(self.opponent_history, opponent_move)
        self.score += round_result


def play_one_round(player1, player2):
    move1 = player1.choose_action()
    move2 = player2.choose_action()

    matrix = [
        [
            [player2.score / (player1.score + player2.score), 0, player1.score / (player1.score + player2.score)],
            [0.7, 0, 0.3],
            [5 / 11, 0, 6 / 11]
        ],
        [
            [0.3, 0, 0.7],
            [1 / 3, 1 / 3, 1 / 3],
            [0.3, 0.5, 0.2]
        ],
        [
            [6 / 11, 0, 5 / 11],
            [0.2, 0.5, 0.3],
            [0.1, 0.8, 0.1]
        ]
    ]

    rand_value = np.random.uniform()
    win_prob = matrix[move1][move2][0]
    draw_prob = matrix[move1][move2][1]

    if rand_value <= win_prob:
        player1.update_after_round(move1, move2, 1)
        player2.update_after_round(move2, move1, 0)
    elif rand_value <= win_prob + draw_prob:
        player1.update_after_round(move1, move2, 0.5)
        player2.update_after_round(move2, move1, 0.5)
    else:
        player1.update_after_round(move1, move2, 0)
        player2.update_after_round(move2, move1, 1)


def monte_carlo(rounds):
    A = StrategyA()
    B = StrategyB()

    for _ in range(rounds):
        play_one_round(A, B)

    print(f"Alice scored: {A.score}")
    print(f"Bob scored:   {B.score}")


if __name__ == "__main__":
    monte_carlo(100000)