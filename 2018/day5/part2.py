from collections import defaultdict

def react_polymer(polymer: list):
  while True:
    starting_len = len(polymer)
    ptr = 0

    while True:
      if ptr + 1 >= starting_len:
        break
      first = str(polymer[ptr])
      second = str(polymer[ptr + 1])

      # make sure they are the same 'type'
      if first.lower() == second.lower():
        if (first.islower() and second.isupper()) or (first.isupper() and second.islower()):
          polymer.pop(ptr)
          polymer.pop(ptr)
          break
      ptr += 1
    ending_len = len(polymer)
    if ending_len == starting_len:
      return len(polymer)


if __name__ == "__main__":
  with open("input.txt", "r") as f:
    original_input_polymer = f.read().strip()

    min_size = None
    min_unit = None
    for unit_type in range(ord('a'), ord('z') + 1):
      f = list(original_input_polymer)
      f[:] = [x for x in f if ord(x.lower()) != unit_type]
      size = react_polymer(f)
      if min_size == None or size < min_size:
        min_size = size
        min_unit = unit_type
    print(f'{chr(min_unit)} - {min_size}')

















