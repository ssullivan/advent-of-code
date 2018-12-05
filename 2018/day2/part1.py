def get_letter_freq(barcode: str) -> tuple:
  freq = {}
  two_count = 0
  three_count = 0
  for i in range(0, len(barcode)):
    slice = barcode[i:i+1]
    if slice == None:
      break
    if slice in freq:
      freq[slice] += 1
    else:
      freq[slice] = 1

  for slice in freq:
    if freq[slice] == 2 and two_count == 0:
      two_count = 1
    elif freq[slice] == 3 and three_count == 0:
      three_count = 1

  return tuple([two_count, three_count])

if __name__ == "__main__":
  freq = 0
  with open("input.txt", "r") as f:
    total_two = 0
    total_three = 0
    for line in f:
      two_result,three_result = get_letter_freq(line)
      total_two += two_result
      total_three += three_result

    print(str(total_two * total_three))