def main():
    with open("1_5.txt", "r") as file:
        genome = file.read().strip()

    k = 9
    l = 500
    t = 3

    patterns = find_clump(genome, k, l, t)
    with open("1_5_output.txt", "w") as file:
        file.write(patterns)

def find_clump(genome, k, l, t):
    patterns = set()

    for i in range(len(genome) - l + 1):
        window = genome[i:i + l]
        freq_map = frequency_map(window, k)
        for pattern, count in freq_map.items():
            if count >= t:
                patterns.add(pattern)
    return " ".join(sorted(patterns))
def frequency_map(text, k):
    patterns = {}

    for i in range(len(text) - k + 1):
        if text[i:i+k] not in patterns:
            patterns[text[i:i+k]] = 1
        else:
            patterns[text[i:i+k]] += 1

    return patterns
main()