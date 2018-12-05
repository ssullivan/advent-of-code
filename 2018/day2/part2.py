
def get_barcode_distance(lhs: str, rhs: str):
  delta = 0
  common = ''
  for i in range(0, len(lhs)):
    x = lhs[i:i+1]
    y = rhs[i:i+1]
    if not(x == y):
      delta = delta + 1
    else:
      common = common + x
  return delta, common

if __name__ == "__main__":
  with open("input.txt", "r") as f:
    barcodes = [line.strip() for line in f]
    barcodes.sort()

    min = None
    shared = None
    for i in range(0, len(barcodes)):
      for j in range(0, len(barcodes)):
        if (i == j):
          continue

        delta, incommon = get_barcode_distance(barcodes[i], barcodes[j])
        print(f'{barcodes[i]} - {barcodes[j]} = {delta}, {incommon}')
        if min == None or delta < min:
          min = delta
          shared = incommon
    print(shared)




