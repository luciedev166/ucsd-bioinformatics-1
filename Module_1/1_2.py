def main():
    with open("1_2.txt", "r") as file:
        text = file.read().strip()
    k = 14
    print(frequent_words(text, k))
def frequent_words(text, k):
    patterns = {}

    for i in range(len(text) - k):
        if text[i:i+k] not in patterns:
            patterns[text[i:i+k]] = 1
        else:
            patterns[text[i:i+k]] += 1

    max_count = max(patterns.values())
    return " ".join([key for key, value in patterns.items() if value == max_count])
main()