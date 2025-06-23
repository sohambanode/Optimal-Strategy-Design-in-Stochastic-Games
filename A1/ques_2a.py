import numpy as np

class Alice:
    def __init__(self):
        self.my_moves = np.array([1, 1])
        self.outcomes = np.array([1, 0])
        self.opp_moves = np.array([1, 1])
        self.total_points = 1

    def decide_move(self):
        last_outcome = self.outcomes[-1]

        if last_outcome == 1:
            win_ratio = 1 - (self.total_points / len(self.outcomes))
            if win_ratio > 6/11:
                return 0  # aggressive
            else:
                return 2  # defensive
        elif last_outcome == 0.5:
            return 0
        else:
            return 1  # balanced

    def update_state(self, my_move, opponent_move, result):
        self.my_moves = np.append(self.my_moves, my_move)
        self.outcomes = np.append(self.outcomes, result)
        self.opp_moves = np.append(self.opp_moves, opponent_move)
        self.total_points += result

class Bob:
    def __init__(self):
        self.my_moves = np.array([1, 1])
        self.outcomes = np.array([0, 1])
        self.opp_moves = np.array([1, 1])
        self.total_points = 1

    def decide_move(self):
        recent_result = self.outcomes[-1]

        if recent_result == 1:
            return 2
        elif recent_result == 0.5:
            return 1
        else:
            return 0

    def update_state(self, my_move, opponent_move, result):
        self.my_moves = np.append(self.my_moves, my_move)
        self.outcomes = np.append(self.outcomes, result)
        self.opp_moves = np.append(self.opp_moves, opponent_move)
        self.total_points += result

def execute_single_round(player_a, player_b):
    move_a = player_a.decide_move()
    move_b = player_b.decide_move()

    matrix = [
        [
            [player_b.total_points / (player_a.total_points + player_b.total_points), 0, player_a.total_points / (player_a.total_points + player_b.total_points)],
            [0.7, 0, 0.3],
            [5/11, 0, 6/11]
        ],
        [
            [0.3, 0, 0.7],
            [1/3, 1/3, 1/3],
            [0.3, 0.5, 0.2]
        ],
        [
            [6/11, 0, 5/11],
            [0.2, 0.5, 0.3],
            [0.1, 0.8, 0.1]
        ]
    ]

    random_val = np.random.rand()

    p_win = matrix[move_a][move_b][0]
    p_draw = matrix[move_a][move_b][1]

    if random_val <= p_win:
        player_a.update_state(move_a, move_b, 1)
        player_b.update_state(move_b, move_a, 0)
    elif random_val <= p_win + p_draw:
        player_a.update_state(move_a, move_b, 0.5)
        player_b.update_state(move_b, move_a, 0.5)
    else:
        player_a.update_state(move_a, move_b, 0)
        player_b.update_state(move_b, move_a, 1)

def simulate_match(total_rounds):
    alice = Alice()
    bob = Bob()

    for _ in range(total_rounds):
        execute_single_round(alice, bob)

    print(f"Final score for Alice: {alice.total_points}")
    print(f"Final score for Bob: {bob.total_points}")

if __name__ == "__main__":
    simulate_match(100000)