if __name__ == "__main__":
  with open("input.txt", "r") as f:
    barcodes = []
    raw_lines = []
    for line in f:
      barcodes.append(set(list(line.replace("\n", ""))))
      raw_lines.append(line)

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


    print(str(lhs_closest) + ", " + raw_lines[lhs_closest])
    print(str(rhs_closest) + ", " + raw_lines[rhs_closest])
    print("".join(list(barcodes[lhs_closest].intersection(barcodes[rhs_closest]))))
    print(closest)
