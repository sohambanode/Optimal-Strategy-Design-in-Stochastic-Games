M = 1000000007

def mod_add(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a + b) % M

def mod_multiply(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a * b) % M

def mod_divide(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return mod_multiply(a, pow(b, M - 2, M))

def game_duration(p, q, k, t, W):
    memo = [0] * (k + W)
    return compute_duration(p, q, k, t, W, memo, k)

def compute_duration(p, q, position, t, W, memo, start):
    if position >= start + W or position <= t:
        return 0
    if memo[position] != 0:
        return memo[position]

    next_up = next_down = 0

    if position + 1 < start + W and position + 1 > t:
        memo[position + 1] = compute_duration(p, q, position + 1, t, W, memo, start)
        next_up = memo[position + 1]

    if position - 1 > t and position - 1 < start + W:
        memo[position - 1] = compute_duration(p, q, position - 1, t, W, memo, start)
        next_down = memo[position - 1]

    memo[position] = 1 + p * next_up + q * next_down
    return memo[position]

print(game_duration(1/2, 1/2, 4, 3, 3))