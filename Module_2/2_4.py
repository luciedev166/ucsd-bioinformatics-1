def main():
    pattern = "AAGCGCATTCC"
    k = 4
    with open("2_4.txt", "r") as file:
        text = file.read().strip()
    
    positions = pattern_positions(text, pattern, k)
    answers = " ".join(map(str, positions))

    with open("2_4_output.txt", "w") as file:
        file.write(answers)

def pattern_positions(text, pattern, k):
    positions = []
    for i in range(len(text)- len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= k:
            positions.append(i)
    return positions

def hamming_distance(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
main()