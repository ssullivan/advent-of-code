import re

class Rect:
  def __init__(self, left: int, top: int, width: int, height: int):
    self._left = left
    self._top = top
    self._width = width
    self._height = height

  def left(self) -> int:
    return self._left

  def top(self) -> int:
    return self._top

  def width(self) -> int:
    return self._width

  def height(self) -> int:
    return self._height


class Claim:
  def __init__(self, id: str, left: int, top: int, width: int, height: int):
    self._id = id
    self._rect = Rect(left, top, width, height)

  def __init__(self, raw_claim: str):
    claim_pattern = re.compile("^(#\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)$")
    match = claim_pattern.match(raw_claim)
    self._id = match.group(1)
    self._rect = Rect(int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)))

  def rect(self) -> Rect:
    return self._rect


def intersect_range(value: int, min: int, max: int) -> bool:
  return value >= min and value <= max

def intersect_rect(lhs: Rect, rhs: Rect) -> bool:
  left_overlap = intersect_range(lhs.left(), rhs.left(), rhs.left() + rhs.width()) or \
    intersect_range(lhs.left(), lhs.left(), lhs.left() + lhs.width())
  right_overlap = intersect_range(lhs.top(), rhs.top(), rhs.top() + rhs.height()) or \
                  intersect_range(lhs.top(), lhs.top(), lhs.top() + lhs.height())
  return left_overlap and right_overlap

def intersect(lhs: Claim, rhs: Claim) -> bool:
  return intersect_rect(lhs.rect(), rhs.rect())



if __name__ == "__main__":
  with open("input.txt", "r") as f:
    claims = [Claim(line.strip()) for line in f]

  print()