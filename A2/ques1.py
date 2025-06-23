def win_probability(p, q, k, N):
    if k == N:
        return 1
    if k == 0:
        return 0

    prob_diff = (q / p) ** k
    success_prob = 1 - prob_diff

    total_diff = (q / p) ** N
    total_success = 1 - total_diff

    return success_prob / total_success

def limit_win_probability(p, q, k):
    return (q / p) ** k

def game_duration(p, q, k, N):
    if k == N or k == 0:
        return 0
    if p == 0:
        return k
    if p == 1:
        return N - k

    factor = (1 / p) - 1
    term_ratio = (1 + factor) / (1 - factor)

    incomplete_sum = (1 - factor ** k)
    complete_sum = (1 - factor ** N)

    expected_correction = (N * incomplete_sum) / complete_sum
    remaining_steps = k - expected_correction

    print(remaining_steps, term_ratio)

    duration = -term_ratio * remaining_steps
    return duration

print(game_duration(1, 0, 10, 50))