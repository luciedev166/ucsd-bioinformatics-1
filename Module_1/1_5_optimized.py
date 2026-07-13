def main():
    with open("1_5.txt", "r") as file:
        genome = file.read().strip()

    k = 9
    l = 500
    t = 3

    patterns = find_clumps_fast(genome, k, l, t)
    print(len(patterns))
def find_clumps_fast(genome, k, L, t):
    clumps = set()
    freq_map = frequency_map(genome[:L], k)

    for pattern, count in freq_map.items():
        if count >= t:
            clumps.add(pattern)

    for i in range(1, len(genome) - L + 1):
        outgoing = genome[i - 1:i - 1 + k]
        freq_map[outgoing] -= 1

        incoming_start = i + L - k
        incoming = genome[incoming_start:incoming_start + k]

        freq_map[incoming] = freq_map.get(incoming, 0) + 1

        if freq_map[incoming] >= t:
            clumps.add(incoming)

    return clumps


def frequency_map(text, k):
    frequencies = {}

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        frequencies[pattern] = frequencies.get(pattern, 0) + 1

    return frequencies
main()