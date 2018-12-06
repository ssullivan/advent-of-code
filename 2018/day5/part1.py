if __name__ == "__main__":
  with open("sample.txt", "r") as f:
    original_input_polymer = f.read().strip()
    original = list(original_input_polymer)
    ptr = 0
    counter = 0
    while True:
      first = str(original.pop(ptr))
      second = str(original.pop(ptr))

      # Cover case aA or Aa
      if not(first.upper() == second or \
        second.upper() == first):
        original.insert(ptr, second)
        original.insert(ptr, first)
        ptr += 2
      else:
       # print(f'removed {first}{second}')
        ptr = 0
      print(f'{len(original)},{ptr}')

      if ptr + 1 >= len(original):
        break

      if counter >= len(original):
        counter = 0

    print("".join(original))














