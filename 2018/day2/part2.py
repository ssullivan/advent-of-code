if __name__ == "__main__":
  with open("sample.txt", "r") as f:
    barcodes = []
    raw_lines = []
    for line in f:
      barcodes.append(set(list(line.replace("\n", ""))))
      raw_lines.append(line.replace("\n", ""))

    len_barcodes = len(barcodes)
    lhs_closest = None
    rhs_closest = None
    closest = None
    for i in range(0, len_barcodes):
      for j in range(0, len_barcodes):
        if i != j:
          lhs = barcodes[i]
          rhs = barcodes[j]

          delta = len(lhs.difference(rhs))

          if closest is None:
            lhs_closest = i
            rhs_closest = j
            closest = delta
          elif delta < closest:
            lhs_closest = i
            rhs_closest = j
            closest = delta

    lhs = raw_lines[lhs_closest]
    rhs = raw_lines[rhs_closest]
    retval = []
    maxI = len(lhs)

    if len(rhs) < len(lhs):
      maxI = len(rhs)

    for i in range(0, maxI):
      if lhs[i:i+1] == rhs[i:i+1]:
        retval.append(lhs[i:i+1])



    print(str(lhs_closest) + ", " + raw_lines[lhs_closest])
    print(str(rhs_closest) + ", " + raw_lines[rhs_closest])
    print("".join(retval))
    print(closest)

#fghij
#fguij
#fgij