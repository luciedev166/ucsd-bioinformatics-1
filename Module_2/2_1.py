def main():
    with open("2_1.txt", "r") as file:
        text = file.read().strip()
    
    results = min_skew_positions(text)
    with open("2_1_output.txt", "w") as file:
        file.write(results)
def min_skew_positions(text):
    skew = [0]

    for i in text:
        if i == "G":
            skew.append(skew[-1] + 1)
        elif i == "C":
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    minimum = min(skew)
    positions = [str(i) for i, value in enumerate(skew) if value == minimum]

    return " ".join(positions)
main()