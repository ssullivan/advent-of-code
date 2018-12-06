if __name__ == "__main__":
  with open("input.txt", "r") as f:
    original_input_polymer = f.read().strip()
    original = list(original_input_polymer)
    ptr = 0
    counter = 0
    while True:

      first = original[ptr]
      second = original[ptr + 1]

      # Cover case aA or Aa
      if not(first.upper() == second or \
        second.upper() == first):
        ptr += 2
      else:
        original.pop(ptr)
        original.pop(ptr)
        ptr = 0
      print(f'{len(original)},{ptr}')

      if ptr + 1 >= len(original):
        break

      if counter >= len(original):
        counter = 0

    print("".join(original))














