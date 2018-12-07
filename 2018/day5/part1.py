from collections import defaultdict, deque

if __name__ == "__main__":
  with open("sample.txt", "r") as f:
    original_input_polymer = f.read().strip()


    original = list(original_input_polymer)

    counter = defaultdict(int)

    changes = 0
    while True:
      starting_len = len(original)
      ptr = 0


      while True:
        if ptr + 1 >= starting_len:
          break

        first = str(original[ptr])
        second = str(original[ptr + 1])

        # make sure they are the same 'type'
        if first.lower() == second.lower():
          if (first.islower() and second.isupper()) or (first.isupper() and second.islower()):
            counter[first] += 1
            original.pop(ptr)
            original.pop(ptr)
            break
        ptr += 1
      ending_len = len(original)
      if ending_len == starting_len:
        break
      print(f'Starting: {starting_len}, Ending: {ending_len}')

    for polymer_class in counter:
      print(f'{polymer_class} = {counter[polymer_class]}')
    print(len(original))
    print("".join(original))













