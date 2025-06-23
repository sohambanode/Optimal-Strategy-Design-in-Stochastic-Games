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
    return mod_multiply(a, pow(b, M-2, M))

# Problem 3b
def optimal_strategy(na, nb, tot_rounds):
    store = []
    save = 0
    for i in range(2 * na + 3 * tot_rounds + 12):
        store.append([])
        for j in range(2 * nb + 3 * tot_rounds + 12):
            store[i].append([])
            for k in range(3 * tot_rounds + 4):
                store[i][j].append(-1)

    for i in range(1, 2 * na + 3 * tot_rounds + 12):
        for j in range(1, 2 * nb + 3 * tot_rounds + 12):
            store[i][j][0] = i / 2

    for k in range(1, 2 * tot_rounds + 2):
        for p in range(1, 2 * na + 2 * tot_rounds + 12):
            for q in range(1, 2 * nb + 2 * tot_rounds + 12):
                i = p / 2
                j = q / 2
                denom = p + q
                if denom == 0:
                    continue

                p1 = (1 / 3 * ((q / denom) * store[int(2 * (i + 1))][int(2 * j)][k - 1] +
                               (p / denom) * store[int(2 * i)][int(2 * (j + 1))][k - 1])
                     + 127 / 330 * store[int(2 * (i + 1))][int(2 * j)][k - 1]
                     + 93 / 330 * store[int(2 * i)][int(2 * (j + 1))][k - 1])
                
                p2 = (14 / 45 * store[int(2 * (i + 1))][int(2 * j)][k - 1]
                     + 5 / 18 * store[int(2 * i + 1)][int(2 * j + 1)][k - 1]
                     + 37 / 90 * store[int(2 * i)][int(2 * (j + 1))][k - 1])
                
                p3 = (21 / 110 * store[int(2 * (i + 1))][int(2 * j)][k - 1]
                     + 13 / 30 * store[int(2 * i + 1)][int(2 * j + 1)][k - 1]
                     + 94 / 330 * store[int(2 * i)][int(2 * (j + 1))][k - 1])

                if i > 0 and j >= 0 and k >= 0:
                    store[p][q][k] = max(p1, p2, p3)
                    if p == (2 * na) and q == (2 * nb) and k == tot_rounds + 1:
                        if store[p][q][k] == p1:
                            save = 1
                        elif store[p][q][k] == p2:
                            save = 2
                        else:
                            save = 3
                else:
                    store[p][q][k] = 0

    print(store[2 * na][2 * nb][tot_rounds])
    if save == 1:
        return [1, 0, 0]
    elif save == 2:
        return [0, 1, 0]
    else:
        return [0, 0, 1]

def expected_points(tot_rounds):
    tot_rounds -= 2
    store = []
    for i in range(tot_rounds + 100):
        store.append([])
        for j in range(tot_rounds + 100):
            store[i].append([])
            for k in range(tot_rounds + 1):
                store[i][j].append(-1)

    for i in range(1, tot_rounds + 100):
        for j in range(1, tot_rounds + 100):
            store[i][j][0] = i / 2

    for k in range(1, tot_rounds + 1):
        for p in range(1, tot_rounds + 30):
            for q in range(1, tot_rounds + 30):
                i = p / 2
                j = q / 2
                denom = p + q
                if denom == 0:
                    continue

                p1 = (1 / 3 * ((q / denom) * store[int(2 * (i + 1))][int(2 * j)][k - 1] +
                               (p / denom) * store[int(2 * i)][int(2 * (j + 1))][k - 1])
                     + 127 / 330 * store[int(2 * (i + 1))][int(2 * j)][k - 1]
                     + 93 / 330 * store[int(2 * i)][int(2 * (j + 1))][k - 1])
                
                p2 = (14 / 45 * store[int(2 * (i + 1))][int(2 * j)][k - 1]
                     + 5 / 18 * store[int(2 * i + 1)][int(2 * j + 1)][k - 1]
                     + 37 / 90 * store[int(2 * i)][int(2 * (j + 1))][k - 1])
                
                p3 = (21 / 110 * store[int(2 * (i + 1))][int(2 * j)][k - 1]
                     + 13 / 30 * store[int(2 * i + 1)][int(2 * j + 1)][k - 1]
                     + 94 / 330 * store[int(2 * i)][int(2 * (j + 1))][k - 1])

                if i > 0 and j >= 0 and k >= 0:
                    store[p][q][k] = max(p1, p2, p3)
                else:
                    store[p][q][k] = 0

    return store[1][1][tot_rounds] + 0.5