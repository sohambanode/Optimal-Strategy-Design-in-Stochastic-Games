def decimalToBinary(num, k_prec):
    binary_str = ""
    int_part = int(num)
    frac_part = num - int_part

    while int_part:
        bit = int_part % 2
        binary_str += str(bit)
        int_part //= 2

    binary_str = binary_str[::-1]
    binary_str += '.'

    for _ in range(k_prec):
        frac_part *= 2
        bit = int(frac_part)
        if bit == 1:
            frac_part -= bit
            binary_str += '1'
        else:
            binary_str += '0'

    return binary_str


def win_probability(p, q, k, N):
    bin_repr = decimalToBinary(k / N, 50)
    return win_prob_binary(p, q, k, N, bin_repr)


def win_prob_binary(p, q, k, N, bin_repr):
    if bin_repr == "0":
        return 0
    if bin_repr == "1":
        return 1

    first_bit = bin_repr[0]
    rest_bits = bin_repr[1:]

    if first_bit == "1":
        return p + q * win_prob_binary(p, q, k - 1, N, rest_bits)
    else:
        return q + p * win_prob_binary(p, q, k - 1, N, rest_bits)


def game_duration(p, q, k, N):
    bin_repr = decimalToBinary(k / N, 50)
    return win_time_prob_binary(p, q, k, N, bin_repr)


def win_time_prob_binary(p, q, k, N, bin_repr):
    if bin_repr == "0":
        return 0
    if bin_repr == "1":
        return 0

    first_bit = bin_repr[0]
    rest_bits = bin_repr[1:]

    if first_bit == "1":
        return 1 + q * win_prob_binary(p, q, k - 1, N, rest_bits)
    else:
        return 1 + p * win_prob_binary(p, q, k - 1, N, rest_bits)


print(win_probability(1, 0, 10, 40))