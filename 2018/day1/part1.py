if __name__ == "__main__":
  freq = 0
  with open("input.txt", "r") as f:
    for line in f:
      freq = freq + int(line)
    print(freq)