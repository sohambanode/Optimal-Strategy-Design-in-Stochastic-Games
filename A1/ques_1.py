MOD = 10**9 + 7

def mod_add(x, y):
    x = (x % MOD + MOD) % MOD
    y = (y % MOD + MOD) % MOD
    return (x + y) % MOD

def mod_mul(x, y):
    x = (x % MOD + MOD) % MOD
    y = (y % MOD + MOD) % MOD
    return (x * y) % MOD

def mod_div(x, y):
    x = (x % MOD + MOD) % MOD
    y = (y % MOD + MOD) % MOD
    return mod_mul(x, pow(y, MOD - 2, MOD))

def compute_probability(alice_wins, bob_wins):
    prob_table = [[-1 for _ in range(101)] for _ in range(101)]
    prob_table[0][0] = 1

    for j in range(100):
        prob_table[0][j + 1] = mod_mul(mod_div(1, j + 2), prob_table[0][j])
    for i in range(100):
        prob_table[i + 1][0] = mod_mul(mod_div(1, i + 2), prob_table[i][0])

    for i in range(1, 100):
        for j in range(1, 100):
            term1 = mod_mul(mod_div(i + 1, i + j + 1), prob_table[i][j - 1])
            term2 = mod_mul(mod_div(j + 1, i + j + 1), prob_table[i - 1][j])
            prob_table[i][j] = mod_add(term1, term2)

    return prob_table[alice_wins - 1][bob_wins - 1]

def compute_expectation(turns):
    memo = [[-1 for _ in range(101)] for _ in range(101)]
    memo[0][0] = 1

    for j in range(100):
        memo[0][j + 1] = mod_mul(mod_div(1, j + 2), memo[0][j])
    for i in range(100):
        memo[i + 1][0] = mod_mul(mod_div(1, i + 2), memo[i][0])

    for i in range(1, 100):
        for j in range(1, 100):
            left = mod_mul(mod_div(i + 1, i + j + 1), memo[i][j - 1])
            right = mod_mul(mod_div(j + 1, i + j + 1), memo[i - 1][j])
            memo[i][j] = mod_add(left, right)

    expected_sum = 0
    for a in range(turns - 1):
        delta = 2 * a - turns + 2
        expected_sum = mod_add(expected_sum, mod_mul(memo[a][turns - a - 2], delta))

    return expected_sum

def compute_variance(turns):
    table = [[-1 for _ in range(101)] for _ in range(101)]
    table[0][0] = 1

    for j in range(100):
        table[0][j + 1] = mod_mul(mod_div(1, j + 2), table[0][j])
    for i in range(100):
        table[i + 1][0] = mod_mul(mod_div(1, i + 2), table[i][0])

    for i in range(1, 100):
        for j in range(1, 100):
            p1 = mod_mul(mod_div(i + 1, i + j + 1), table[i][j - 1])
            p2 = mod_mul(mod_div(j + 1, i + j + 1), table[i - 1][j])
            table[i][j] = mod_add(p1, p2)

    variance_sum = 0
    for a in range(turns - 1):
        term = 2 * a - turns + 2
        squared_term = mod_mul(term, term)
        variance_sum = mod_add(variance_sum, mod_mul(table[a][turns - a - 2], squared_term))

    return variance_sum

# Sample Output
print(compute_probability(36, 66))
print(compute_expectation(66))
print(compute_variance(66))