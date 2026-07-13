def main():
    pattern = "ATCGC"
    with open("2_5.txt", "r") as file:
        text = file.read().strip()
    
    k = 2

    print(pattern_positions(text, pattern, k))
def pattern_positions(text, pattern, k):
    
    count = 0
    for i in range(len(text)- len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= k:
            count += 1
    return count

def hamming_distance(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
main()