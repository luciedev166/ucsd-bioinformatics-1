def main():
    text = "GAGCCACCGCGATA"
    
    results = skew_array(text)
    print(results)
def skew_array(text):
    skew = [0]

    for i in text:
        if i == "G":
            skew.append(skew[-1] + 1)
        elif i == "C":
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    return " ".join(map(str, skew))
main()