import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1, 1])
        self.results = np.array([1, 0])
        self.opp_play_styles = np.array([1, 1])
        self.points = 1

    def play_move(self):
        last_result = self.results[-1]
        if last_result == 1:
            if (1 - (self.points / len(self.results))) > (6 / 11):
                return 0
            return 2
        elif last_result == 0.5:
            return 0
        return 1

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
        recent = self.results[-1]
        if recent == 1:
            return 2
        elif recent == 0.5:
            return 1
        return 0

    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result


def simulate_round(alice, bob):
    alice_move = alice.play_move()
    bob_move = bob.play_move()

    payoff_matrix = [
        [[bob.points / (alice.points + bob.points), 0, alice.points / (bob.points + alice.points)], [0.7, 0, 0.3], [5 / 11, 0, 6 / 11]],
        [[0.3, 0, 0.7], [1 / 3, 1 / 3, 1 / 3], [0.3, 0.5, 0.2]],
        [[6 / 11, 0, 5 / 11], [0.2, 0.5, 0.3], [0.1, 0.8, 0.1]]
    ]

    random_value = np.random.uniform()
    p_win = payoff_matrix[alice_move][bob_move][0]
    p_draw = payoff_matrix[alice_move][bob_move][1]

    if random_value <= p_win:
        alice.observe_result(alice_move, bob_move, 1)
        bob.observe_result(bob_move, alice_move, 0)
    elif random_value <= p_win + p_draw:
        alice.observe_result(alice_move, bob_move, 0.5)
        bob.observe_result(bob_move, alice_move, 0.5)
    else:
        alice.observe_result(alice_move, bob_move, 0)
        bob.observe_result(bob_move, alice_move, 1)


def monte_carlo(target_wins, alice, bob):
    rounds_played = 2  # Already 2 rounds initialized
    alice_wins = 1

    while alice_wins < target_wins:
        rounds_played += 1
        a_move = alice.play_move()
        b_move = bob.play_move()

        payoff_matrix = [
            [[bob.points / (alice.points + bob.points), 0, alice.points / (bob.points + alice.points)], [0.7, 0, 0.3], [5 / 11, 0, 6 / 11]],
            [[0.3, 0, 0.7], [1 / 3, 1 / 3, 1 / 3], [0.3, 0.5, 0.2]],
            [[6 / 11, 0, 5 / 11], [0.2, 0.5, 0.3], [0.1, 0.8, 0.1]]
        ]

        rand_val = np.random.uniform()
        win_prob = payoff_matrix[a_move][b_move][0]
        draw_prob = payoff_matrix[a_move][b_move][1]

        if rand_val <= win_prob:
            alice.observe_result(a_move, b_move, 1)
            alice_wins += 1
            bob.observe_result(b_move, a_move, 0)
        elif rand_val <= win_prob + draw_prob:
            alice.observe_result(a_move, b_move, 0.5)
            bob.observe_result(b_move, a_move, 0.5)
        else:
            alice.observe_result(a_move, b_move, 0)
            bob.observe_result(b_move, a_move, 1)

    return rounds_played


def estimate_tau(T):
    all_counts = []
    alice = Alice()
    bob = Bob()

    for _ in range(100):
        count = monte_carlo(T, alice, bob)
        all_counts.append(count)

        alice.__init__()  # reset Alice
        bob.__init__()    # reset Bob

    return np.mean(all_counts)


result = estimate_tau(100)
print(result)