if __name__ == "__main__":
  with open("input.txt", "r") as f:
    original_input_polymer = f.read().strip()

    original = list(original_input_polymer)
    ptr = 0
    changes = 0
    while True:
      if ptr + 1 >= len(original):
        if changes <= 0:
          break
        ptr = 0
        changes = 0

      first = original[ptr]
      second = original[ptr + 1]

      # Cover case aA or Aa
      if not(first.upper() == second or \
             second.upper() == first):
        ptr += 1
      else:
        original.pop(ptr)
        original.pop(ptr)
        ptr = 0
        changes += 1

      if len(original) % 10 == 0:
        print(f'{len(original)},{ptr}')





    print("".join(original))














