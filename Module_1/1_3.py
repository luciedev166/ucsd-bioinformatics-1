def main():
    with open("1_3.txt", "r") as file:
      text = file.read().strip()
    print(reverse_complement(text))

def reverse_complement(text):
    base = {
      "A":"T",
      "T":"A",
      "C":"G",
      "G":"C",
   } 
    rev = ""
    for i in text:
        rev += base[i]
    return rev[::-1]
main()