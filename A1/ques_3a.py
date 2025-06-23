import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1, 1])
        self.results = np.array([1, 0])
        self.opp_play_styles = np.array([1, 1])
        self.points = 1

    def play_move(self):
        # Alice's strategy: based on win rate threshold
        if (1 - (self.points / len(self.results))) > 15 / 44:
            return 0  # attack
        else:
            return 2  # defend

    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result


class Bob:
    def __init__(self):
        self.past_play_styles = np.array([1, 1])
        self.results = np.array([0, 1])
        self.opp_play_styles = np.array([1, 1])
        self.points = 1

    def play_move(self):
        # Bob plays randomly
        move = np.random.choice([0, 1, 2])
        return move

    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result


def simulate_round(alice, bob, payoff_matrix):
    alice_move = alice.play_move()
    bob_move = bob.play_move()

    rand_value = np.random.uniform(0, 1)
    if rand_value <= payoff_matrix[alice_move][bob_move][0]:
        alice.observe_result(alice_move, bob_move, 1)
        bob.observe_result(bob_move, alice_move, 0)
    elif rand_value <= payoff_matrix[alice_move][bob_move][1] + payoff_matrix[alice_move][bob_move][0]:
        alice.observe_result(alice_move, bob_move, 0.5)
        bob.observe_result(bob_move, alice_move, 0.5)
    else:
        alice.observe_result(alice_move, bob_move, 0)
        bob.observe_result(bob_move, alice_move, 1)


def monte_carlo(num_rounds):
    alice = Alice()
    bob = Bob()
    payoff_matrix = [
        [[bob.points / (alice.points + bob.points), 0, alice.points / (bob.points + alice.points)], [0.7, 0, 0.3], [5 / 11, 0, 6 / 11]],
        [[0.3, 0, 0.7], [1 / 3, 1 / 3, 1 / 3], [0.3, 0.5, 0.2]],
        [[6 / 11, 0, 5 / 11], [0.2, 0.5, 0.3], [0.1, 0.8, 0.1]]
    ]

    for _ in range(num_rounds):
        simulate_round(a, b, payoff_matrix)


if __name__ == "__main__":
    a = Alice()
    b = Bob()
    monte_carlo(num_rounds=10**5)
    print(f"Alice has scored {a.points}")
    print(f"Bob has scored {b.points}")