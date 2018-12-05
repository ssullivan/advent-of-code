if __name__ == "__main__":

  freq_inputs = []
  with open("input.txt", "r") as f:
    for line in f:
      freq_inputs.append(int(line))

  # this is our starting
  freq = 0
  freq_counters = {}
  found = False
  while not(found):
    for input in freq_inputs:
      freq = freq + input

      if freq in freq_counters:
        freq_counters[freq] += 1
      else:
        freq_counters[freq] = 1

      if freq_counters[freq] == 2:
        print(freq)
        found = True
        break

