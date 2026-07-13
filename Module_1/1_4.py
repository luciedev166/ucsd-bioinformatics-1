def main():
    pattern = "CTTGATCAT"
    with open("1_4.txt", "r") as file:
        text = "".join(file.read().split())
    
    positions = (pattern_matching(text, pattern))
    answer = " ".join(map(str, positions))

    with open("1_4_output.txt", "w") as file:
        file.write(answer)
def pattern_matching(text, pattern):
    positions = []
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if text[i:i+k] == pattern:
            positions.append(i)
    return positions

main()