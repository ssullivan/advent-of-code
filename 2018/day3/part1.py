import re


class Rect:
  def __init__(self, left: int, top: int, width: int, height: int):
    self._left = left
    self._top = top
    self._width = width
    self._height = height
    self._right = self._left + self._width
    self._bottom = self._top + self._height

  def left(self) -> int:
    return self._left

  def right(self) -> int:
    return self._left + self._width

  def bottom(self) -> int:
    return self._top + self._height

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
    # #{id} @ {left},{top}: {width}x{height}
    self._raw = raw_claim
    claim_pattern = re.compile("^(#\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)$")
    match = claim_pattern.match(raw_claim)
    self._id = match.group(1)
    self._rect = Rect(int(match.group(2)), int(match.group(3)),
                      int(match.group(4)), int(match.group(5)))

  def rect(self) -> Rect:
    return self._rect

  def __str__(self):
    return self._raw


def intersect_range(value: int, min: int, max: int) -> bool:
  return value >= min and value <= max


def intersect_rect(a: Rect, b: Rect) -> bool:
  return (intersect_range(b.left(), a.left(), a.right()) or
          intersect_range(a.left(), b.left(), b.right())) and \
         (intersect_range(b.top(), a.top(), a.bottom()) or
          intersect_range(a.top(), b.top(), b.bottom()))


def intersect(lhs: Claim, rhs: Claim) -> bool:
  return intersect_rect(lhs.rect(), rhs.rect())


def intersect_point(a: Rect, row, col):
  return intersect_rect(a, Rect(col, row, 0, 0))


if __name__ == "__main__":
  with open("input.txt", "r") as f:
    claims = [Claim(line.strip()) for line in f]

    state_space = {}

    total = 0
    for claim in claims:
      for i in range(claim.rect().left(), claim.rect().right()):
        for j in range(claim.rect().top(), claim.rect().bottom()):
          key = str(i) + "." + str(j)
          if key not in state_space:
            state_space[key] = set()
          state_space[key].add(claim)

    total = 0
    for key in state_space:
      if len(state_space[key]) >= 2:
        total += 1
    print(f'{total}')
